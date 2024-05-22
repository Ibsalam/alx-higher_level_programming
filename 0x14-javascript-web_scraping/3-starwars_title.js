#!/usr/bin/node
const axios = require('axios');
const movieId = process.argv[2];
const API_ENDPOINT = 'https://swapi-api.hbtn.io/api/films/';

axios(API_ENDPOINT + movieId, function (err, response, body) {
if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
