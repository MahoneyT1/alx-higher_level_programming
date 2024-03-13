#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!isNaN(arg1) || !isNaN(arg2)) {
    const first = parseInt(arg1, 10);
    const second = parseInt(arg2, 10);

    let sum = add(first, second);
    console.log(sum);

} else {
    console.log(NaN)
}

function add(a, b) {
    return a + b;
}
