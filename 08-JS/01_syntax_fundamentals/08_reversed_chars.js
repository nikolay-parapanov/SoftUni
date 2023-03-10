function reversedChars(a,b,c) {
    let arr = [];
    arr.push(a);
    arr.push(b);
    arr.push(c);
    // console.log(arr)
    reversedArr = arr.reverse();
    // console.log(reversedArr);
    output = '';
    for (const item of reversedArr) {
        output += item + ' ';
    }
    console.log(output.trim());
}

reversedChars('A',
'B',
'C'
);

reversedChars('1',
'L',
'&'
);