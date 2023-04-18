#!/usr/bin/node

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (err, resp, body) {
  if (err) return;
  console.log('code:', resp.statusCode);
});
