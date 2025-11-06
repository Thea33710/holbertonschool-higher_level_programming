#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
    console.log(0);
}
else {
    let max = Math.max(...args);
    let filtered = args.filter(n => n !== max);
    let secondMax = filtered.length ? Math.max(...filtered) : 0;
    console.log(secondMax);
}
