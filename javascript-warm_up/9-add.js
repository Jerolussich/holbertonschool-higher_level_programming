#!/usr/bin/node

const args = process.argv;

console.log(factorial(Number(args[2])));

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
