#!/usr/bin/node
'use strict';
const myArgs = process.argv.slice(2);
function Add (a, b) { console.log(a + b); }
Add(parseInt(myArgs[0]), parseInt(myArgs[1]));
