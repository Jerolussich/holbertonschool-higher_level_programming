#!/usr/bin/node
const args = process.argv.slice(2);
const toPrint = args[0];

if (toPrint) {
  console.log(toPrint);
} else {
  console.log('No argument');
}
