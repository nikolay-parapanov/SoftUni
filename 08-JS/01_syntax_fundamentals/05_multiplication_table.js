function multiplicationTable(number) {

    for (let index = 1; index <= 10; index++) {
        result = number * index;
        console.log(`${number} X ${index} = ${result}`)
    }

}

multiplicationTable(5);