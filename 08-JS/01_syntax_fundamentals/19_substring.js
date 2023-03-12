function solve(wordInput, sentence) {
    wordInputLower = wordInput.toLowerCase();
    arrSentence = sentence.split(' ');
    flag = false;
    for (const word of arrSentence) {
        // console.log(word.toLowerCase());
        if (word.toLowerCase() === wordInputLower) {
            flag = true;
        }
    }
    flag
        ? console.log(`${wordInput}`)
        : console.log(`${wordInput} not found!`)
}


solve('javascript',
    'JavaScript is the best programming language'
);

solve('python',
    'JavaScript is the best programming language'
);