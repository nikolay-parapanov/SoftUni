function printAndSum (startNumber, endNumber){
let arr = [];
sum = 0;
    for (let index = startNumber; index <= endNumber; index++) {
        arr.push(index);
        sum += index;
        // console.log(arr);
    }
    console.log(`${arr.join(' ')}`);
    console.log(`Sum: ${sum}`);
}


printAndSum (5,10);
printAndSum (0, 26);
printAndSum (50,60);