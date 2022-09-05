#!/usr/bin/node
'use strict';
const myArgs = process.argv.slice(2);
const num = parseInt(myArgs[0]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; num > i; i++) console.log('X'.repeat(num));
}
