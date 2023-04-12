#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (isNaN(args[2]) || isNaN(args[3])) {
  console.log('NaN');
} else {
  add(parseInt(args[2]), parseInt(args[3]));
}

function add (a, b) {
  console.log(a + b);
}
