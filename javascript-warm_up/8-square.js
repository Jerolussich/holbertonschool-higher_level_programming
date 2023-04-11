#!/usr/bin/node

let args = process.argv
let size = Number(args[2])

if ((size != size))
    console.log("Missing size");
else
    for (let i = 0; i < size; i++)
    {
        for (let i = 0; i < size; i++)
            process.stdout.write("X");
        console.log()
    }
