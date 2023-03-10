function sameNumbers(numberInput) {
    let arr = numberInput.toString().split('');
    // console.log(arr);
    flag = true;
    sum = 0;
    for (const element of arr) {
        if (element !== arr[0]) {
            flag = false;
            break;
        }
    }

    for (const element of arr) {
        sum += Number(element);
    }

    (flag === false)
        ? console.log('false')
        : console.log('true')
    console.log(sum);
}


sameNumbers(2222222);
sameNumbers(1234);