#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

fs.writeFile(args[2], args[3], 'utf-8', function (err) {
  if (err) {
    console.error(err);
  }
});
