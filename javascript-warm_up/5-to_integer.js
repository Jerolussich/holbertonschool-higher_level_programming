#!/usr/bin/node

let args = process.argv
let argument_given = Number(process.argv[2])

if (!(argument_given != argument_given))
    console.log(`My number ${argument_given}`)
