function vacation(numberOfPeople, typeOfGroup, dayOfWeek) {
    switch (typeOfGroup) {
        case 'Students':
            switch (dayOfWeek) {
                case 'Friday':
                    pricePerPerson = 8.45;
                    break;
                case 'Saturday':
                    pricePerPerson = 9.8;
                    break;
                case 'Sunday':
                    pricePerPerson = 10.46;
                    break;
            }
        case 'Business':
            switch (dayOfWeek) {
                case 'Friday':
                    pricePerPerson = 10.9;
                    break;
                case 'Saturday':
                    pricePerPerson = 15.6;
                    break;
                case 'Sunday':
                    pricePerPerson = 16;
                    break;
            }
        case 'Regular':
            switch (dayOfWeek) {
                case 'Friday':
                    pricePerPerson = 15;
                    break;
                case 'Saturday':
                    pricePerPerson = 20;
                    break;
                case 'Sunday':
                    pricePerPerson = 22.50;
                    break;
            }
    }
    priceAfterDiscount = 1;
    if (typeOfGroup === 'Students' && numberOfPeople >= 30) {
        priceAfterDiscount = 0.85;
    }
    else if (typeOfGroup === 'Business' && numberOfPeople >= 100) {
        numberOfPeople -= 10;
    }
    else if (typeOfGroup === 'Regular' && (numberOfPeople >= 10 && numberOfPeople<=20)) {
        priceAfterDiscount = 0.95;
    }
    
    totalPrice = numberOfPeople * pricePerPerson * priceAfterDiscount;
    result = totalPrice.toFixed(2);
    console.log(`Total price: ${result}`);
}

vacation(30,
    "Students",
    "Sunday"
)

vacation(40,
    "Regular",
    "Saturday"
)