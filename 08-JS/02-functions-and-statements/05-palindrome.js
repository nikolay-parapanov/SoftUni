function palindrome(numbers) {
    numbers
        .forEach((num) => {
            console.log(isPalindrome(num));
        });


    function isPalindrome(num) {
        let reversed = Number([...num.toString()].reverse().join(''));
        return num === reversed;
    }

}

palindrome([123,323,421,121]);
palindrome([32,2,232,1010]);