function solve(sentence) {

    let arrSentence = sentence.split(' ');
    let primaryWordsArr = [];
    let finalWordsArr = [];
    let flag = true;
    for (let index = 0; index < arrSentence.length; index++) {
        if (arrSentence[index][0] === '#' && arrSentence[index].length > 1) {
            primaryWordsArr.push(arrSentence[index]);
        }
    }
    // console.log(primaryWordsArr);
    for (const word of primaryWordsArr) {
        wordCheck = word.substring(1,100000).toLowerCase();
        flag = true; 
        for (const letter of wordCheck) {
            // console.log(letter.charCodeAt(0));
            if (letter.charCodeAt(0) < 97 || letter.charCodeAt(0) > 122) {
                flag = false;
                break;
            }
        }
        if (flag === true) {
            console.log(word.substring(1,100000));
        }
    }
}


solve('Nowadays everyone uses # to tag a #special word in #socialMedia');
solve('The symbol # is known #variously in English-speaking #regions as the #number sign');