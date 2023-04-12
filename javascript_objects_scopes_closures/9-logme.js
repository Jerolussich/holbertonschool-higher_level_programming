#!/usr/bin/node

let previous_output = 0;

exports.logMe =
function (item) {
  console.log(`${previous_output}: ${item}`);
  previous_output += 1;
};
