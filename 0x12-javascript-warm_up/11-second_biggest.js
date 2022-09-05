#!/usr/bin/node
'use strict';
const myArgs = process.argv.slice(2);
myArgs.sort(function factorial (a, b) { return b - a; });
const res = myArgs.length < 2 ? 0 : myArgs[1];
console.log(res);
