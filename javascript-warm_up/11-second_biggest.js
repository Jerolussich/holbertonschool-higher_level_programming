#!/usr/bin/node

let args = process.argv;

if (args.length < 4)
    console.log("0");
else
{
    let biggest_number = -Infinity;

    for (let i = 2; i < args.length; i++)
        if (Number(args[i]) > biggest_number)
            biggest_number = Number(args[i]);     
    console.log(biggest_number);
}
