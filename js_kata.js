// 02/01/2024
// Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

// function smash (words) {
//     return words.join(' ')
// };

// let words = ['hello', 'world', 'this', 'is', 'great']
// console.log(smash(words)) // returns "hello world this is great"

// // 03/01/2024
// // Given an array of integers, return a new array with each value doubled.
// // For example:
// // [1, 2, 3] --> [2, 4, 6]

// function maps(x){
//     return x.map(x => x * 2)
// }

// console.log(maps([1, 2, 3])) // returns [2, 4, 6]

// 04/01/2024
function countPositivesSumNegatives(input) {
    if (input == null || input.length == 0) {
        return [];
    }
    let countPositives = 0;
    let sumNegatives = 0;
    for (let i = 0; i < input.length; i++) {
        let num = input[i]; // Added this line to assign the current number to the 'num' variable
        if (num > 0) {
            countPositives += 1;
        } else { // Changed 'if' to 'else if' to avoid unnecessary checks
            sumNegatives += num;
        }
    }
    return [countPositives, sumNegatives];
}

output = countPositivesSumNegatives([-2, -1, 0, 1, 2]);
console.log(output);

