#!/usr/bin/node

const argumentGiven = parseInt(process.argv[2]);

if (!isNaN(argumentGiven)) {
  console.log(`My number: ${argumentGiven}`);
} else {
  console.log('Not a number');
}
