function matrixPrinting (numberInput){
    
    for (let row = 0; row < numberInput; row++) {
        console.log((`${numberInput} `).repeat(numberInput));
    }
}

matrixPrinting(3);