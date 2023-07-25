#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  console.log(response.statusCode)
});
