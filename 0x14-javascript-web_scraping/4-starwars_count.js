#!/usr/bin/node
/**
 * script that pritns the title of a Star Wars movie
 * where the epidsode number matches a given integer.
 */
const request = require('request');
const url = process.argv[2];
const result = [];
const ID = 18;

request(url, (err, res, body) => {
  if (!err) {
    result.push(...JSON.parse(body).results);
    const count = result.filter(e => e.characters.includes(`https://swapi-api.hbtn.io/api/people/${ID}/`));
    console.log(count.length);
  } else console.log(err);
});
