#!/usr/bin/node
exports.addMeMaybe = function (num, callback) {
  callback(++num);
};
