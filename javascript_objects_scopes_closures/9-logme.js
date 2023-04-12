#!/usr/bin/node

let previousOutput = 0;

exports.logMe = function (item) {
  console.log(`${previousOutput}: ${item}`);
  previousOutput += 1;
};
