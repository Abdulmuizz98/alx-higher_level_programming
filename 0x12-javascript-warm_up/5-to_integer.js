#!/usr/bin/node
'use strict';
const myArgs = process.argv.slice(2);
isNaN(parseInt(myArgs[0]))
  ? console.log('Not a number')
  : console.log('My number:', parseInt(myArgs[0]));
