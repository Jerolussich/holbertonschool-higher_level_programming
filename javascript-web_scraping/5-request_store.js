#!/usr/bin/node

let request = require(`request`);
let args = process.argv;
let fs = require('fs');

const options = {
    url: args[2],
    method: `GET`
}

request(options, function(err, resp, body) {
    let data = String(body)


fs.writeFile(args[3], data, encoding="utf-8", function(err) {
    if (err)
    {
        return console.log(err);
    }
})});
