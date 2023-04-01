function oddOccurences(input) {
    arrInput = input.split(' ');
    arrLower = [];
    finalCount = {};

    for (const item of arrInput) {
        let itemLower = item.toLowerCase();
        arrLower.push(itemLower);
    }

    for (const itemLower of arrLower) {

        if (itemLower in finalCount) {
            finalCount[itemLower] += 1;
        } else {
            finalCount[itemLower] = 1;
        }
    }
    // console.log(finalCount);
    let output = [];
    let entries = Object.entries(finalCount);
    for ([key, value] of entries) {
        if (value % 2 !== 0) {
            output.push(key);
        }
    }
    console.log(output.join(' '));
}



oddOccurences(
    'Java C# Php PHP Java PhP 3 C# 3 1 5 C#'
)