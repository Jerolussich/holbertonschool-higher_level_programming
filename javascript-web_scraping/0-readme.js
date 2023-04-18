#!/usr/bin/node

const args = process.argv;
let fs = require('fs');

fs.readFile(args[2], encode="utf-8", function(err, data){

    if (err) {
        console.log(err);
    }
    else
        console.log(data);
});
