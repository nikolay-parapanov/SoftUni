function factoriaDivision(firstNumber, secondNumber) {

    return (getFactorial(firstNumber)/ getFactorial(secondNumber)).toFixed(2);

    function getFactorial(number) {
        if (number === 1) {
            return 1;
        } else {
            return number * getFactorial(number - 1);
        }
    }

}
console.log(factoriaDivision(5,2));
console.log(factoriaDivision(6,2));