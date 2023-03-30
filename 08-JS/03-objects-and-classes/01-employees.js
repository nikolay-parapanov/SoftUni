function employees(arrayInput) {
    let database = {};
    for (let index = 0; index < arrayInput.length; index++) {
        recordName = arrayInput[index];
        personalNumber = recordName.length;
        database[recordName] = recordName.length;
    }

    for (const key in database) {
        console.log(`Name: ${key} -- Personal Number: ${database[key]}`)
    }
}


employees(
    [
        'Silas Butler',
        'Adnaan Buckley',
        'Juan Peterson',
        'Brendan Villarreal'
    ]

)