#!/usr/bin/node
const args = process.argv.slice(2);
const to_print = args[0];

if (to_print) {
  console.log(to_print);
} else {
  console.log('No argument');
}
