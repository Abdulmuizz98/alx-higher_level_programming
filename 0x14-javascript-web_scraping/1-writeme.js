#!/usr/bin/node
/**
 * script that writes a string to a file.
 */
// const path = require('path')
const fs = require('fs');
const args = process.argv.slice(2);
// const filePath = path.join(__dirname, process.argv[2])

fs.writeFile(args[0], args[1], { encoding: 'utf-8' }, (err) => {
  if (err) console.log(err);
});
