#!/usr/bin/node
/**
 * script that gets the contents of a webpage and stores it ina file.
 */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, res, body) => {
  if (!err) {
    fs.writeFile(path, body, { encoding: 'utf-8' }, (error) => {
      if (error) console.log(err);
    });
  } else console.log(err);
});
