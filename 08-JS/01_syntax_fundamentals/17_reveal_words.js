function solve(string, sentence) {
    wordsToReplaceInSentece = string.split(', ');
    // console.log(wordsToReplaceInSentece);
    wordsFromSentence = sentence.split(' ');

    for (const word of wordsToReplaceInSentece) {
        // console.log(`word: ${word}`);
        // console.log(`word.length: ${word.length}`);
        for (let index = 0; index < wordsFromSentence.length; index++) {
            // console.log(wordsFromSentence[index]);
            // console.log(wordsFromSentence[index].length);
            
            if (wordsFromSentence[index][0] === '*' && word.length === wordsFromSentence[index].length) {
                wordsFromSentence[index] = word;
            }
        }
    }
    output = wordsFromSentence.join(' ');
    console.log(output.trim());
}

solve('great',
    'softuni is ***** place for learning new programming languages'
);

solve('learning, great',
    'softuni is ***** place for ******** new programming languages'
);