const PENDING = "pending";
const FULFILLED = "fulfilled";
const REJECTED = "rejected";

function microEvent(cb) {
	if (process && process.nextTick) {
		process.nextTick(cb);
	} else if (MutationObserver) {
		let observer = new MutationObserver(cb);
		let p = document.createElement("p");
		observer.observe(p, {
			childList: true,
		});
		p.innerHTML = 1;
	} else {
		setTimeout(cb, 0);
	}
}
function isPromise(obj) {
	return !!(obj && typeof obj === "object" && typeof obj.then === "function");
}
microEvent(() => {});
class Pro {
	constructor(executor) {
		this._value = undefined;
		this._status = PENDING;
		this._handlers = [];
		try {
			executor(this._resolve.bind(this), this._reject.bind(this));
		} catch (error) {
			this._reject(error);
		}
	}
	_resolve(data) {
		this._changeStatus(FULFILLED, data);
	}
	_reject(data) {
		this._changeStatus(REJECTED, data);
	}
	_changeStatus(status, data) {
		if (this._status !== PENDING) return;
		this._status = status;
		this._value = data;
		this._runHandlers();
	}
	then(fulfilled, rejected) {
		return new Pro((resolve, reject) => {
			this._pushHandler(fulfilled, FULFILLED, resolve, reject);
			this._pushHandler(rejected, REJECTED, resolve, reject);
			this._runHandlers();
		});
	}
	catch(rejected) {
		return this.then(undefined, rejected);
	}
	_pushHandler(executor, status, resolve, reject) {
		this._handlers.push({
			executor,
			status,
			resolve,
			reject,
		});
	}
	_runHandlers() {
		if (this._status === PENDING) return;
		let handler;
		while ((handler = this._handlers.shift())) {
			this._runOneHandler(handler);
		}
	}
	_runOneHandler({ executor, status, resolve, reject }) {
		microEvent(() => {
			if (this._status !== status) return;
			if (typeof executor !== "function") {
				this._status === FULFILLED
					? resolve(this._value)
					: reject(this._value);
			} else {
				try {
					let res = executor(this._value);
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

let pro1 = new Pro((resolve, reject) => {
	// resolve(1);
	reject(2);
});
let pro2 = pro1
	.then(
		(resp) => {
			return resp;
		},
		(e) => e
	)
	.catch((e) => {
		console.log(3);
		return 3;
	});
setTimeout(() => {
	console.log(pro1, "----", pro2);
}, 1000);
