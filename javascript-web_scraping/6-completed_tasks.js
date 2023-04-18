#!/usr/bin/node

const request = require('request');
const args = process.argv;

const options = {
  url: args[2],
  method: 'GET'
};

const userData = {};

request(options, function (err, resp, body) {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);

  data.forEach(task => {
    if (!userData[task.userId] && task.completed === true) {
      userData[task.userId] = 0;
      userData[task.userId]++;
    }
    if (task.completed === true) {
      userData[task.userId]++;
    }
  });

  console.log(userData);
});
