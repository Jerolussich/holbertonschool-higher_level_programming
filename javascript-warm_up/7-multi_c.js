#!/usr/bin/node

let args = process.argv
let argument_given = Number(process.argv[2])

if ((argument_given != argument_given))
    console.log('Missing number of occurrences');
else
    {
    for (let i = 0; i < argument_given; i++)
        console.log('C is fun');
}
