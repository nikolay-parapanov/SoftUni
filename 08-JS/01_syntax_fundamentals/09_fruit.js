function fruit(typeOfFruit, weightInGrams, pricePerKg){
    let totalCost = 0;
    kg = weightInGrams/1000;
    totalCost = (kg * pricePerKg).toFixed(2);
    console.log(`I need $${totalCost} to buy ${kg.toFixed(2)} kilograms ${typeOfFruit}.`);
}

fruit('orange', 2500, 1.80);
fruit('apple', 1563, 2.35);