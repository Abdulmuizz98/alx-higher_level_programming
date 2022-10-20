#!/usr/bin/node
/**
 * script that pritnsall the characters of a Star Wars movie
 */
const request = require('request');
let movie, result, peopleResult;
const movId = process.argv[2];
const filmUrl = "https://swapi-api.hbtn.io/api/films/"
const peopleUrl = "https://swapi-api.hbtn.io/api/people/"

request(filmUrl, (err, res, bod) => {
  if (!err) {
    result = [...JSON.parse(bod).results];
    movie = result[movId-1];
	  request(peopleUrl, (error, response, body) => {
            if (!error) {
	      peopleResult = [...JSON.parse(body).results]
	      peopleResult = peopleResult.filter(e => movie.characters.includes(e.url))
		console.log(peopleResult);
	    }
	    else console.log(err);
	  })
  } else console.log(err);
});
