function perfectNumber(numberInput) {
    let flag = true;
    let sum = 0;

    for (let index = 1; index < Math.floor(numberInput / 2); index++) {
        if (numberInput % index === 0) {
            sum += index;
            // console.log(sum);
        }
    }
    // console.log(sum); 
    // console.log(flag);
    (flag === true && sum*2 === numberInput)
        ? output = "We have a perfect number!"
        : output = "It's not so perfect."

    return output
}

perfectNumber(1236498);
