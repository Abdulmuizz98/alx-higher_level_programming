#!/usr/bin/node
exports.callMeMoby = function (num, callback) {
  for (let i = 0; num > i; i++) callback();
};
