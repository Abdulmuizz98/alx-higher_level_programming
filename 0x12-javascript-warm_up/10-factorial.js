#!/usr/bin/node
'use strict';
const myArgs = process.argv.slice(2);
function factorial (a) { if (a === 1 || isNaN(a)) { return 1; } else { return a * factorial(a - 1); } }
console.log(factorial(parseInt(myArgs[0])));
