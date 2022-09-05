#!/usr/bin/node
'use strict';
const myArgs = process.argv.slice(2);
const res = myArgs.length ? (myArgs.length === 1 ? 'Argument found' : 'Arguments found') : 'No argument';
console.log(res);
