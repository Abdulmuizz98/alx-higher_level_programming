#!/usr/bin/node
'use strict';
const myArgs = process.argv.slice(2);
const res = myArgs[0] !== undefined ? myArgs[0] : 'No argument';
console.log(res);
