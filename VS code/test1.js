class A {
	constructor(a, b) {
		Object.assign(this, [1, 2], b);
	}
}
var a = { name: "小明" };
var b = { age: 12 };
let c = new A(a, b);
console.log(c.name, c.age);
