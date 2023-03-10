function sumDigits(number) {
    let len = number.toString().length;
    let sum = 0;
    while (len > 1) {
        last_digit = number % 10;
        number = Math.floor(number / 10);
        len -= 1;
        sum += last_digit;
        // console.log(last_digit);
        // console.log(number);
    }
    sum += number;
    console.log(sum);
}

sumDigits(245678);
sumDigits(97561);
sumDigits(543);