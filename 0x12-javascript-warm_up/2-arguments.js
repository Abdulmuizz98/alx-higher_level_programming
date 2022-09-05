#!/usr/bin/node
'use strict';
const myArgs = process.argv.slice(2);
const res = myArgs.length ? 'Arguments found' : 'No argument';
console.log(res);
