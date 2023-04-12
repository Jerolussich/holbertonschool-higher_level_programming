#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;

  for (const item of list) {
    if (item !== searchElement) { continue; }
    occurrences++;
  }

  return occurrences;
};
