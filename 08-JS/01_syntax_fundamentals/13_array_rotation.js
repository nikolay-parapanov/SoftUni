function solve(numbers, rotations) {
    for (let index = 0; index < rotations; index++) {
        helper = numbers.shift();
        numbers.push(helper);
    }
    console.log(numbers.join(' '));

}

solve([51, 47, 32, 61, 21], 2);
solve([32, 21, 61, 1], 4);