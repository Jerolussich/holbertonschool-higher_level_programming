#!/usr/bin/node

const args = process.argv;
const argumentGiven = Number(process.argv[2]);

if (!(argumentGiven != argumentGiven)) { 
    console.log(`My number: ${argumentGiven}`); 
}
else {
    console.log('Not a number');
}
