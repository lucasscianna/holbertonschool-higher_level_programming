#!/usr/bin/node
let first = 0;
let second = 0;

for (let i = 2; i < process.argv.length; i++) {
  if (parseInt(process.argv[i]) > first) {
    second = first;
    first = parseInt(process.argv[i]);
  } else if (parseInt(process.argv[i]) > second) {
    second = parseInt(process.argv[i]);
  }
}
console.log(second);
