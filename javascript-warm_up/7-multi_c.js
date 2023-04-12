#!/usr/bin/node

const argumentGiven = Number(process.argv[2]);

if (isNaN(argumentGiven)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argumentGiven; i++) {
    console.log('C is fun');
  }
}
