#!/usr/bin/node

exports.esrever = function (list) {
  let size = list.length - 1;
  let index = 0;
  const new_list = [];

  for (let i = size; list[size]; size--, index++) {
    new_list[index] = list[size];
  }

  return new_list;
};
