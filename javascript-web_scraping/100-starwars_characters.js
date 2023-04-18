#!/usr/bin/node

const request = require('request');
const args = process.argv;

const options = {
    url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`,
    method: 'GET'
  };

request(options, function(err, resp, body) {
    let data = JSON.parse(body)

    data.characters.forEach(url_chars => {

        const options_2 = {
            url: url_chars,
            method: 'GET'
        };
        request(options_2, function(err, resp, body) {
            let chars_data = JSON.parse(body)
        
            console.log(chars_data.name);
    })
    });
});
