function charsInRange ( firstCharInput, secondCharInput) {
    firstCharInputAscii = Math.min(firstCharInput.charCodeAt(0), secondCharInput.charCodeAt(0));
    secondCharInputAscii = Math.max(firstCharInput.charCodeAt(0), secondCharInput.charCodeAt(0));
    outputArr = [];

    for (let index = firstCharInputAscii+1; index < secondCharInputAscii; index++) {
        outputArr.push(String.fromCharCode(index));
    }

    return outputArr.join(" ");
}

console.log(charsInRange('a', 'd'));
console.log(charsInRange('C',
'#'
));
