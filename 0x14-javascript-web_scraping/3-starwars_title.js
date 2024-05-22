#!/usr/bin/node
const axios = require('axios');
const movieId = process.argv[2];
const API_ENDPOINT = 'https://swapi-api.hbtn.io/api/films/';

axios.get(API_ENDPOINT + movieId)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    if (error.response) {
      console.log('Error code: ' + error.response.status);
    } else {
      console.log(error.message);
    }
  });
