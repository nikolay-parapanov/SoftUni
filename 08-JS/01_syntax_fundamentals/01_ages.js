function age(a) {
    if (a >= 0 && a <= 2) {
        result = 'baby';
    }
    else if (a>=3 && a <=13){
        result = 'child';
    }
    else if (a>= 14 && a<= 19) {
        result = 'teenager';
    }
    else if (a>=20 && a<= 65) {
        result = 'adult';
    }
    else if (a>=66){
        result = 'elder'
    } else {
        result = 'out of bounds';
    }
    console.log(result)
}


age(20)
age(1)
age(100)
age(-1)