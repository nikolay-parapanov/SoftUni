function vacation(numberOfPeople, typeOfGroup, dayOfWeek) {
    switch (typeOfGroup) {
        case 'Students':
            if (dayOfWeek === 'Friday') {
                pricePerPerson = 8.45;
            }
            else if (dayOfWeek === 'Saturday') {
                pricePerPerson = 9.8;
            }
            else if (dayOfWeek === 'Sunday') {
                pricePerPerson = 10.46;
            }
            break;
        case 'Business':
            if (dayOfWeek === 'Friday') {
                pricePerPerson = 10.9;
            }
            else if (dayOfWeek === 'Saturday') {
                pricePerPerson = 15.6;
            }
            else if (dayOfWeek === 'Sunday') {
                pricePerPerson = 16;
            }
            break;
        case 'Regular':
            if (dayOfWeek === 'Friday') {
                pricePerPerson = 15;
            }
            else if (dayOfWeek === 'Saturday') {
                pricePerPerson = 20;
            }
            else if (dayOfWeek === 'Sunday') {
                pricePerPerson = 22.5;
            }
            break;
    }
    // console.log(pricePerPerson);
    priceAfterDiscount = 1;
    if (typeOfGroup === 'Students' && numberOfPeople >= 30) {
        priceAfterDiscount = 0.85;
    }
    else if (typeOfGroup === 'Business' && numberOfPeople >= 100) {
        numberOfPeople -= 10;
    }
    else if (typeOfGroup === 'Regular' && (numberOfPeople >= 10 && numberOfPeople <= 20)) {
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