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

// // 04/01/2024
// function countPositivesSumNegatives(input) {
//     if (input == null || input.length == 0) {
//         return [];
//     }
//     let countPositives = 0;
//     let sumNegatives = 0;
//     for (let i = 0; i < input.length; i++) {
//         let num = input[i]; // Added this line to assign the current number to the 'num' variable
//         if (num > 0) {
//             countPositives += 1;
//         } else { // Changed 'if' to 'else if' to avoid unnecessary checks
//             sumNegatives += num;
//         }
//     }
//     return [countPositives, sumNegatives];
// }

// output = countPositivesSumNegatives([-2, -1, 0, 1, 2]);
// console.log(output);

// 05/01/2024
// Rock Paper Scissors
// Let's play! You have to return which player won! In case of a draw return Draw!.
// Examples(Input1, Input2 --> Output):
// "scissors", "paper" --> "Player 1 won!"
// "scissors", "rock" --> "Player 2 won!"
// "paper", "paper" --> "Draw!"

// const rps = (p1, p2) => {
//     if (p1 == p2) return 'Draw!';
//     if (p1 == 'rock' & p2 == 'scissors') return 'Player 1 won!';
//     if (p1 == 'paper' & p2 == 'rock') return 'Player 1 won!';
//     if (p1 == 'scissors' & p2 == 'paper') return 'Player 1 won!';
//     else return 'Player 2 won';
// };

// console.log(rps('scissors', 'paper'));

// 8 kyu - Keep up the hoop
// Alex just got a new hula hoop, he loves it but feels discouraged because his
//  little brother is better than him
// Write a program where Alex can input (n) how many times the hoop goes round
//  and it will return him an encouraging message :)
// If Alex gets 10 or more hoops, return the string "Great, now move on to
//  tricks".
// If he doesn't get 10 hoops, return the string "Keep at it until you get it".

// function hoopCount (n) {
//     if (n < 10 ) return "Keep at it until you get it";
//     else return "Great, now move on to tricks";
//  }

// console.log(hoopCount(10));

// 06/01/2024
// This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

// function simpleMultiplication(number) {
//     if (number % 2 == 0) return number * 8;
//     else return number * 9;
//   }

//   console.log(simpleMultiplication(4));

// 07/01/2024
// Copilot kata
// 7 kyu - Sum of two lowest positive integers
// Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
// No floats or non-positive integers will be passed.
// For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
// [10, 343445353, 3453445, 3453545353453] should return 3453455.

// function sumTwoSmallestNumbers(numbers) {
//   numbers.sort();
//   return [numbers[0], numbers[1]];
// }

// console.log(sumTwoSmallestNumbers([3,2,1]));

// codewars kata:
// 8 kyu - Invert values
// Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
// invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
// invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
// invert([]) == []
// You can assume that all values are integers. Do not mutate the input array/list.

// function invert(array) {
//   let newArray = [];
//   for (let i = 0; i < array.length; i++) {
//     newArray.push(-array[i]);
//   }
//   return newArray;
// };

// const invert = array => array.map(num => -num);

// const array = [2,2,3,4,5];
// console.log(invert(array));

// 08/01/2024
// codewars kata
// 8 kyu - Twice as old
// Your function takes two arguments:
// current father's age (years)
// current age of his son (years)
// Сalculate how many years ago the father was twice as old as his son (or in
//  how many years he will be twice as old). The answer is always greater or
//  equal to 0, no matter if it was in the past or it is in the future.

// function twiceAsOld(dadYearsOld, sonYearsOld) {
//     let dadAge = dadYearsOld - sonYearsOld;
//     let sonAge = 0
//     for (let i = 0; i < 500; i++) {
//         sonAge++;
//         dadAge++;
//         if (dadAge == 2 * sonAge) {
//             return Math.abs(dadAge - dadYearsOld);
//         }
//     }
// }

// console.log(twiceAsOld(40,2));

// dadsAge = a + n
// childAge = b + n
// Then we can write a general formula that establishes this relationship and substitute the values from our previous expressions
// dadsAge = 2 * childAge
// a + n = 2 * (b + n)
// Finally solve for n
// a + n = 2 * (b + n)
// a + n = 2b + 2n -n -n
// a = n + 2b -2b -2b
// a - 2b = n

/* 09/01/2024
7 kyu - Get the Middle Character
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
#Input
A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.
#Output
The middle character(s) of the word represented as a string.
*/

// function getMiddle(s) {
//     if (s.length % 2 != 0) {
//         let middle = ( s.length + 1 ) / 2;
//         return s.charAt(middle - 1);
//     } else {
//         let middle = s.length / 2
//         return s.slice(middle - 1, middle + 1);
//     }
// }

// console.log(getMiddle('barney'));

/* 10/01/2024
8 kyu - Correct the mistakes of the character recognition software
Character recognition software is widely used to digitise printed texts. Thus 
the texts can be edited, searched and stored on a computer.
When documents (especially pretty old ones written with a typewriter), are 
digitised character recognition softwares often make mistakes.
Your task is correct the errors in the digitised text. You only have to handle 
the following mistakes:
S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.
*/

//
// function correct(string) {
//     let newString = '';
//     for (let i = 0; i < string.length; i++) {
//         if (string[i] == '5') {
//             newString += 'S';
//         } else if (string[i] == '0') {
//             newString += 'O';
//         } else if (string[i] == '1') {
//             newString += 'I';
//         } else {
//             newString += string[i];
//         }
//     }
// }

// correct = s => s.replace(/0/g,'O').replace(/1/g,'I').replace(/5/g,'S')

// console.log(correct('Te5t'));

// 8 kyu - Remove exclamation marks
// ExclamationMarks which removes all exclamation marks from a given string.

// removeExclamationMarks = s => s.replaceAll('!', '')

// console.log(removeExclamationMarks('!test!'));

// 11/01/2024
// 7 kyu - Reverse words
// Complete the function that accepts a string parameter, and reverses each
//  word in the string. All spaces in the string should be retained.
// Examples
// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

// reverse_words = () => { return string.reverse() };

function reverseWords(string) {
    let words = string.split(' ');
    let reversedWords = words.map(word => word.split('').reverse().join(''));
    return reversedWords.join(' ');
}

let string = 'Hello World!';
console.log(reverseWords(string));