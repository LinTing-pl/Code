let ls = ["30 2"];
let [n, m] = ls[0].split(" ").map((v) => +v);
let res = [];
dfs([]);
console.log(res.length);
function dfs(arr) {
  if (arr.length === n) {
    res.push(arr);
    return;
  }
  for (let i = 1; i <= m; i++) {
    if (i !== sum(arr)) {
      dfs(arr.concat(i));
    }
  }
}
function sum(arr) {
  let total = 0;
  arr.map((v) => {
    total += v;
  });
  return total;
}
