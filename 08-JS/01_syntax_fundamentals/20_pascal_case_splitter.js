function solve(stringInput) {
    finalArr = [];
    currentWordArr = [];

    stringArr = stringInput.split('');

    while (stringArr.length >0) {
        if (stringArr[0].charCodeAt(0) >= 65 && stringArr[0].charCodeAt(0) <= 90){
            if (currentWordArr.length>0){
                finalArr.push(currentWordArr.join(''));
                currentWordArr=[];
            }
            currentWordArr.push(stringArr[0]);
        } else {
            currentWordArr.push(stringArr[0]);
        }
        stringArr.shift();
        // console.log(currentWordArr);
    }
    finalArr.push(currentWordArr.join(''));
    console.log(finalArr.join(', '));

}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan');
solve ('HoldTheDoor');
solve ('ThisIsSoAnnoyingToDo');
