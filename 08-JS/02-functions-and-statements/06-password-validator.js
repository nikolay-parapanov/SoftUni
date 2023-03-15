function passwordValidator(stringInput) {
    let flagLength = false;
    let flagOnlyLettersAndNumbers = true;
    let flagTwoOrMoreDigits = false;

    arrStringInput = [...stringInput];
    lengthCheck(arrStringInput);

    function lengthCheck(arrStringInput) {
        if ((arrStringInput.length >= 6) && (arrStringInput.length <= 10)) {
            return flagLength = true;
        } else return flagLength = false;
    }

    for (let index = 0; index < arrStringInput.length; index++) {
        // console.log(arrStringInput[index].charCodeAt(0));
        if (!((arrStringInput[index].charCodeAt(0) >= 48 && arrStringInput[index].charCodeAt(0) <= 57) || (arrStringInput[index].charCodeAt(0) >= 65 && arrStringInput[index].charCodeAt(0) <= 90) || (arrStringInput[index].charCodeAt(0) >= 97 && arrStringInput[index].charCodeAt(0) <= 122))) {
            flagOnlyLettersAndNumbers = false;
            // console.log(flagOnlyLettersAndNumbers);
            break;
        }
    };

    
    let digitsCounter = 0;
    for (let index = 0; index < arrStringInput.length; index++) {
        if (arrStringInput[index].charCodeAt(0) >= 48 && arrStringInput[index].charCodeAt(0) <= 57) {
            digitsCounter++;
        }
    }
    (digitsCounter >= 2)
        ? flagTwoOrMoreDigits = true
        : flagTwoOrMoreDigits = false

    // console.log(flagLength, flagOnlyLettersAndNumbers, flagTwoOrMoreDigits)

    output = ''
    if (flagLength === true && flagOnlyLettersAndNumbers === true && flagTwoOrMoreDigits === true) {
        output += 'Password is valid'
    } else {
        if (flagLength !== true) {
            output += 'Password must be between 6 and 10 characters\n'
        }
        if (flagOnlyLettersAndNumbers !== true) {
            output += 'Password must consist only of letters and digits\n'
        }
        if (flagTwoOrMoreDigits < 2) {
            output += 'Password must have at least 2 digits'
        }
    }
    return output;
}

console.log(passwordValidator('Pa$s$'));