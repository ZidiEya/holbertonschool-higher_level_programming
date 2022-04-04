#!/usr/bin/node
// script that computes and prints a factorial
const { argv } = require('process');

console.log(fact(parseInt(argv[2])));

function fact (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return (num * fact(num - 1));
}
