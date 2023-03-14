function oddAndEvenSum(numberInput) {
 
    numberInputAsString = String(numberInput);
    arr = [...numberInputAsString];
 
    let sumEven = 0;
    let sumOdd = 0;
 
    output = '';

    for (let index = 0; index < arr.length; index++) {
        if (arr[index] % 2 === 0) {
            sumEven += Number(arr[index]);
        } else sumOdd += Number(arr[index]);
    }

    return output += `Odd sum = ${sumOdd}, Even sum = ${sumEven}`
}

console.log(oddAndEvenSum(3495892137259234));