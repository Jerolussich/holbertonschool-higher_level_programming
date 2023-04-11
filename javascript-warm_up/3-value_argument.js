#!/usr/bin/node

const args = process.argv;
let to_print = args[2];

if ((args.length) == 2)
    console.log('No argument');
else
    console.log(to_print);
