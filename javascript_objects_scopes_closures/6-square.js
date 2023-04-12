#!/usr/bin/node

const Square = require('./5-square');

module.exports =
  class Square extends Square {
    charPrint (c = 'X') {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  };
