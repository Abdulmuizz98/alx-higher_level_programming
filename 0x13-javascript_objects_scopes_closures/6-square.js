#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c = 'X') {
    for (let i = 0; this.height > i; i++) console.log(c.repeat(this.width));
  }
};
