#!/usr/bin/node

const request = require('request');

const options = {
  url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`,
  method: 'GET'
};

request(options, function (err, resp, body) {
  if (err) return;
  console.log(JSON.parse(body).title);
});
