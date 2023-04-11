#!/usr/bin/node

const args = process.argv;
const argument_given = Number(process.argv[2]);

if (!(argument_given != argument_given)) { 
    console.log(`My number: ${argument_given}`); 
}
else {
    console.log('Not a number');
}
