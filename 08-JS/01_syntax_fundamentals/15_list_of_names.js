function solve (names) {
    let sortedNamesAsc = [...names].sort((aName, bName) => {
        let result = aName.localeCompare(bName);
        return result;
    });
    
    for (let index = 0; index < sortedNamesAsc.length; index++) {
        console.log(`${index+1}.${sortedNamesAsc[index]}`)
        
    }
}

solve(["John", "Bob", "Christina", "Ema"]);