#!/usr/bin/node
/**
 * script that reads and prints the content of a file
 */
// const path = require('path')
const fs = require('fs');

// const filePath = path.join(__dirname, process.argv[2])

fs.readFile(process.argv[2], { encoding: 'utf-8' }, (err, data) => {
  if (!err) {
    console.log(data);
  } else {
    console.log(err);
  }
});
