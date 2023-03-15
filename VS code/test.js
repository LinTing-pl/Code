const execute = async () => {
  pool = [];
  for (let i = 0; i < 10; i++) {
    let pro = new Promise((resolve) => {
      console.log("in");
      setTimeout(() => {
        resolve(1);
      }, 3000);
    });
    pro.then((resp) => {
      let index = pool.findIndex((v) => v === pro);
      pool.splice(index);
      console.log("then");
    });
    pool.push(pro);
    if (pool.length === 2) {
      console.log(pool.length, "before");
      await Promise.race(pool);
      console.log(pool.length, "after");
    }
  }
};
execute();
