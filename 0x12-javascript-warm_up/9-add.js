#!/usr/bin/node

const com = process.argv;

if (com.length < 4 ) {
    console.log(NaN);
    return
}
const first = parseInt(com[2]);
const second = parseInt(com[3]);

function add(a, b) {
    if (isNaN(a)=== true || isNaN(b) === true){
        return NaN
    }
    return a + b;
}
let sum = add(first, second);
console.log(sum);
