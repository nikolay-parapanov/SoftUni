function solve(numbers) {
    sortedNumbers = [...numbers];

    sortedNumbers.sort(function (a, b) {
        return a - b
    });

    // console.log(sortedNumbers);
    result = [];

    for (let index = 1; index <= numbers.length; index++) {
        if (index % 2 === 0) {
            result.push(sortedNumbers.pop());
        } else {
            result.push(sortedNumbers.shift());
        }
    }
    return result;
}


solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);
