#!/usr/bin/node
exports.addMeMaybe = function (num, callback) {
  ++num;
  callback(num);
};
