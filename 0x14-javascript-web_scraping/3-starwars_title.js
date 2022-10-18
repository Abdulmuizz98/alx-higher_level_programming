#!/usr/bin/node
/**
 * script that pritns the title of a Star Wars movie
 * where the epidsode number matches a given integer.
 */
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
  if (!err) console.log(JSON.parse(body).title);
  else console.log(err);
});
