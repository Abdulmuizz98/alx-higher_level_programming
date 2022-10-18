#!/usr/bin/node
/**
 * script that displays the status code of a GET request.
 */
// const path = require('path')
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) console.log('code: ', res && res.statusCode);
  else console.log(err);
});
