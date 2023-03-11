function solve(numberAsString, ...operations) {
    let number = Number(numberAsString);
    for (const operation of operations) {
        switch (operation) {
            case 'chop':
                number = number / 2;
                break;
            case 'dice':
                number = Math.sqrt(number);
                break;
            case 'spice':
                number += 1;
                break;
            case 'bake':
                number = number * 3;
                break;
            case 'fillet':
                number = number * 0.8;
                break;
        }
        console.log(number);
    }

}

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop');
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet');
