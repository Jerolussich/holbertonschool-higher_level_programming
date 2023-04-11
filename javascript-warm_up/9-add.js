#!/usr/bin/node

let args = process.argv

console.log(add(Number(args[2]), Number(args[3])));

function add(a, b)
{
    return (a + b)
}
