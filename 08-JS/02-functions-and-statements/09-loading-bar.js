function loadingBar(number) {
    let output = '';
    if (number === 100) {
        output = '100% Complete!\n' + '[%%%%%%%%%%]';
    } else {
        bar = `[${'%'.repeat(number / 10)}` + `${'.'.repeat((100 - number) / 10)}]`
        firstLine = `${number}% ${bar}`;
        output = firstLine + '\n' + 'Still loading...';
    }

    return output;
}

console.log(loadingBar(20));