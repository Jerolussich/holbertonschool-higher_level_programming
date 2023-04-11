#!/usr/bin/node

const args = process.argv;
console.log(Factorial(args[2]));

function Factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * Factorial(n - 1);
  }
}
