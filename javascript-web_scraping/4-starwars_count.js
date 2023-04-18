#!/usr/bin/node

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

let count = 0;

request(options, function (err, resp, body) {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body).results;

  data.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes('18')) {
        count += 1;
      }
    });
  });

  console.log(count);
});
