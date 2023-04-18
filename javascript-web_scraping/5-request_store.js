#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const args = process.argv;

const options = {
  url: args[2],
  method: 'GET'
};

request(options, function (err, resp, body) {
  if (err) {
    console.log(err);
    return;
  }

  const data = String(body);
  fs.writeFile(args[3], data, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
