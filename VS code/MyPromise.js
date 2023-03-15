const PENDING = "pending"; //等待状态
const FULFILLED = "fulfilled"; //完成状态
const REJECTED = "rejected"; //失败状态

/**
 * 将任务放入微任务队列
 * @param {Function} fn
 */
function runMicro(fn) {
	if (process && process.nextTick) {
		process.nextTick(fn);
	} else if (MutationObserver) {
		let observer = new MutationObserver(fn);
		let p = document.createElement("p");
		observer.observe(p, { childList: true });
		p.innerHTML = 1;
	} else {
		setTimeout(fn);
	}
}

/**
 * 判断对象是否符合Promise A+规范
 * @param {*} obj
 * @return {Boolean}
 */
function isPromise(obj) {
	return !!(obj && typeof obj === "object" && typeof obj.then === "function");
}
class MyPromise {
	/**
	 * @param {Function} executor 执行器
	 */
	constructor(executor) {
		this._status = PENDING;
		this._value = undefined;
		this._handlers = [];
		try {
			executor(this._resolve.bind(this), this._reject.bind(this));
		} catch (error) {
			this._reject(error);
		}
	}

	/**
	 * 改变状态
	 * @param {String} status 状态
	 * @param {*} value 数据
	 */
	_changeStatus(status, value) {
		if (this._status !== PENDING) return;
		this._status = status;
		this._value = value;
		this._runHandlers();
	}

	/**
	 * 调用该方法，将MyPromise状态转为FULFILLED
	 * @param {*} value
	 */
	_resolve(value) {
		this._changeStatus(FULFILLED, value);
	}

	/**
	 * 调用该方法，将MyPromise状态转为REJECTED
	 * @param {*} value
	 */
	_reject(value) {
		this._changeStatus(REJECTED, value);
	}

	/**
	 * resolve()的回调
	 * @param {*} fulfilled
	 * @param {*} rejected
	 * @return {MyPromise}
	 */
	then(fulfilled, rejected) {
		return new MyPromise((resolve, reject) => {
			this._pushHandler(fulfilled, FULFILLED, resolve, reject);
			this._pushHandler(rejected, REJECTED, resolve, reject);
			this._runHandlers();
		});
	}

	/**
	 * reject()的回调
	 * @param {Function} rejected
	 * @return {*}
	 */
	catch(rejected) {}

	/**
	 * 存储then的resolve和reject事件
	 * @param {*} executor
	 * @param {*} status
	 * @param {*} resolve
	 * @param {*} reject
	 */
	_pushHandler(executor, status, resolve, reject) {
		this._handlers.push({
			executor,
			status,
			resolve,
			reject,
		});
	}

	/**
	 * 执行_handlers : Array中存储的handler : Object
	 */
	_runHandlers() {
		if (this._status === PENDING) return;
		while (this._handlers[0]) {
			let handler = this._handlers[0];
			this._runOneHandler(handler);
			this._handlers.shift();
		}
	}

	/**
	 * 执行一个handler
	 * @param {Function} handler
	 * @return {*}
	 */
	_runOneHandler({ executor, status, resolve, reject }) {
		runMicro(() => {
			if (this._status !== status) return;
			if (typeof executor !== "function") {
				this._status === FULFILLED
					? resolve(this._value)
					: reject(this._value);
			} else {
				try {
					let res = executor();
					if (isPromise(res)) {
						res.then(resolve, reject);
					} else {
						resolve(res);
					}
				} catch (error) {
					reject(error);
				}
			}
		});
	}
}

let pro = new MyPromise((resolve, reject) => {
	console.log(11);
	// resolve(1);
	reject(2);
});
let pro1 = pro.then(
	function A(resp) {
		console.log(1);
		return resp;
	},
	function B(error) {
		console.log(2);
		return error;
	}
);
setTimeout(() => {
	console.log(pro, "---", pro1);
}, 1000);
