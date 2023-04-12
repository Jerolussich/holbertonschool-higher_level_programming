#!/usr/bin/node

exports.esrever = function (list) {
  let size = list.length - 1;
  let index = 0;
  const newList = [];

  for (; list[size]; size--, index++) {
    newList[index] = list[size];
  }

  return newList;
};
