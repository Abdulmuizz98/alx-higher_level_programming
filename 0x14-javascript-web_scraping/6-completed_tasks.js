#!/usr/bin/node
/**
 * script that computes the number of tasks completed by user id.
 */
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    let resArr = JSON.parse(body);
    resArr = resArr.filter(e => e.completed);
    resArr = resArr.reduce((p, c) => {
      if (p[c.userId]) p[c.userId]++;
      else p[c.userId] = 1;
      return p;
    }, {});
    console.log(resArr);
  } else console.log(err);
});
