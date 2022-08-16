#!/usr/bin/node
const x = process.argv[2];
function factorial (x) {
  if (isNaN(x) || x === 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(factorial(parseInt(x)));
