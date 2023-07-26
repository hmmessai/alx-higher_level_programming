#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTodosByUser = todos.reduce((accumulator, todo) => {
    if (todo.completed) {
      accumulator[todo.userId] = (accumulator[todo.userId] || 0) + 1;
    }
    return accumulator;
  }, {});

  Object.entries(completedTodosByUser).forEach(([userId, count]) => {
    console.log(`${userId}: ${count}`);
  });
});

