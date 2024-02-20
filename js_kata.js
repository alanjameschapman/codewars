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

// function reverseWords(string) {
//     let words = string.split(' ');
//     let reversedWords = words.map(word => word.split('').reverse().join(''));
//     return reversedWords.join(' ');
// }

// let string = 'Hello World!';
// console.log(reverseWords(string));

// 12/01/2024
// 8 kyu - Convert a string to an array
// Write a function to split a string and convert it into an array of words.
// e.g.
// string_to_array("Robin Singh") => ["Robin", "Singh"]
// string_to_array("CodeWars") => ["CodeWars"]
// Note: no need to worry about punctuation

// function stringToArray(string) {
//     return string.split(' ');
// }

// console.log(stringToArray('Hello World!'));

// 13/01/2024
// 8 kyu - Square(n) Sum
// Complete the square sum function so that it squares each number passed into
//  it and then sums the results together.
// For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
// My solution:
// function squareSum(numbers) {
//     let sum = 0;
//     for (let i = 0; i < numbers.length; i++) {
//         sum += numbers[i] ** 2;
//     }
//     return sum;
// }
// Best solution:
// function squareSum(numbers){
//     return numbers.reduce(function(sum, n){
//       return (n*n) + sum;
//     }, 0)
//   }

// let numbers = [1, 2, 2];
// console.log(squareSum(numbers));

// 14/01/2024
// 7 kyu - Descending Order
// Your task is to make a function that can take any non-negative integer as a
//  argument and return it with its digits in descending order. Essentially,
//  rearrange the digits to create the highest possible number.
// Examples:
// Input: 21445 Output: 54421
// Input: 145263 Output: 654321
// Input: 1254859723 Output: 9875543221

// function descendingOrder(n) {
//     return parseInt(String(n).split('').sort().reverse().join(''));
// }

// console.log(descendingOrder(213));

// 15/01/2024
// 8 kyu - Will you make it?
// You were camping with your friends far away from home, but when it's time to
//  go back, you realize that you fuel is running out and the nearest pump is
//  50 miles away! You know that on average, your car runs on about 25 miles per
//  gallon. There are 2 gallons left. Considering these factors, write a
//  function that tells you if it is possible to get to the pump or not. Function
//  should return true if it is possible and false if not.

// const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
//     if ( distanceToPump <= mpg * fuelLeft) {
//         return true;
//     }
//   };

// const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
//     return distanceToPump <= mpg * fuelLeft;
// };

//   console.log(zeroFuel(51, 25, 2))

// 16/01/2024
// 7 kyu - Beginner Series #3 Sum of Numbers
// Given two integers a and b, which can be positive or negative, find the sum
//  of all the numbers between including them too and return it. If the two
//  numbers are equal return a or b.
// Note: a and b are not ordered!
// Examples:
// GetSum(1, 0) == 1   // 1 + 0 = 1
// GetSum(1, 2) == 3   // 1 + 2 = 3
// GetSum(0, 1) == 1   // 0 + 1 = 1
// GetSum(1, 1) == 1   // 1 Since both are same
// GetSum(-1, 0) == -1 // -1 + 0 = -1
// GetSum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

// function getSum(a, b) {
//   let sum = 0;
//   const min = Math.min(a, b);
//   const max = Math.max(a, b);
//   for (let i = min; i <= max; i++) {
//     sum += i;
//   }
//   return sum;
// }

// console.log(getSum(0, 3));

// 17/01/2024
// 7 kyu - Growth of a Population
// In a small town the population is p0 = 1000 at the beginning of a year. The
//  population regularly increases by 2 percent per year and moreover 50 new
//  inhabitants per year come to live in the town. How many years does the town
//  need to see its population greater or equal to p = 1200 inhabitants?
// At the end of the first year there will be:
// 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
// At the end of the 2nd year there will be:
// 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an
//  integer **)
// At the end of the 3rd year there will be:
// 1141 + 1141 * 0.02 + 50 => 1213
// It will need 3 entire years.
// More generally given parameters:
// p0, percent, aug (inhabitants coming or leaving each year), p (population to
//  surpass)
// the function nb_year should return n number of entire years needed to get a
//  population greater or equal to p.
// aug is an integer, percent a positive or null number, p0 and p are positive
//  integers (> 0)
// Examples:
// nb_year(1500, 5, 100, 5000) -> 15
// nb_year(1500000, 2.5, 10000, 2000000) -> 10

// function nbYear(p0, percent, aug, p) {
//   let nb_year = 0;
//   while (p0 < p) {
//     p0 += Math.floor(p0 * (percent / 100) + aug);
//     nb_year++;
//   }
//   return nb_year;
// }

// console.log(nbYear(1500, 5, 100, 5000));
// console.log(nbYear(1500000, 2.5, 10000, 2000000));

// 18/01/2024
// 7 kyu - Ones and Zeros
// Given an array of ones and zeroes, convert the equivalent binary value to an
//  integer.
// Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
// Examples:
// Testing: [0, 0, 0, 1] ==> 1
// Testing: [0, 0, 1, 0] ==> 2
// Testing: [0, 1, 0, 1] ==> 5
// Testing: [1, 0, 0, 1] ==> 9
// Testing: [0, 0, 1, 0] ==> 2
// Testing: [0, 1, 1, 0] ==> 6
// Testing: [1, 1, 1, 1] ==> 15
// Testing: [1, 0, 1, 1] ==> 11
// However, the arrays can have varying lengths, not just limited to 4.

// const binaryArrayToNumber = arr => {
//   return parseInt(arr.join(''), 2);
// }

// console.log(binaryArrayToNumber([0, 0, 0, 1]));

// 19/01/2024
// 7 kyu - Two to One
// Take 2 strings s1 and s2 including only letters from ato z. Return a new
//  sorted string, the longest possible, containing distinct letters,
//  each taken only once - coming from s1 or s2.
// Examples:
// a = "xyaabbbccccdefww"
// b = "xxxxyyyyabklmopq"
// longest(a, b) -> "abcdefklmopqwxy"
// a = "abcdefghijklmnopqrstuvwxyz"
// longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

// function longest(s1, s2) {
//   let s3 = s1 + s2;
//   let s4 = s3.split('').sort();
//   let s5 = s4.filter((item, index) => s4.indexOf(item) === index);
//   return s5.join('');
// }

// console.log(longest('xyaabbbccccdefww', 'xxxxyyyyabklmopq'));

// 21/01/2024
// 8 kyu - Reversed Strings
// Complete the solution so that it reverses the string passed into it.
// 'world'  =>  'dlrow'

// function solution(str) {
//   return str.split('').reverse().join('');
// }

// console.log(solution('string'));

// 22/01/2024
// 8 kyu - Grasshopper - Messi goals function
// Messi is a soccer player with goals in three leagues:
// LaLiga
// Copa del Rey
// Champions
// Complete the goals function to return his total goals (the sum) for all three
//  leagues.
// Note: the parameter for this function will always be a valid number.
// Ex:
// goals(5,10,2) == 5+10+2 = 17

// function goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
//   return laLigaGoals + copaDelReyGoals + championsLeagueGoals;
// }

// console.log(goals(5,10,2));

// 23/01/2024
// 7 kyu - Exes and Ohs
// Check to see if a string has the same amount of 'x's and 'o's. The method
//  must return a boolean and be case insensitive. The string can contain any
//  char.
// Examples input/output:
// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

// // my solution
// function XO(str) {
//   let x = 0;
//   let o = 0;
//   for (let s = 0; s < str.length; s++) {
//     if (str[s].toLowerCase() === 'x') {
//       x += 1;
//     } else if (str[s].toLowerCase() === 'o') {
//       o += 1;
//     }
//   }
//   if (x === o) {
//     return true;
//   } else {
//     return false;
//   }
// }

// // best solution:
// function XO(str) {
//   let x = str.match(/x/gi);
//   let o = str.match(/o/gi);
//   return (x && x.length) === (o && o.length);
// }

// console.log(XO('xoxox'));

// 24/01/2024
// 7 kyu - Find the next perfect square!
// You might know some pretty large perfect squares. But what about the NEXT one?
// Complete the findNextSquare method that finds the next integral perfect
//  square after the one passed as a parameter. Recall that an integral perfect
//  square is an integer n such that sqrt(n) is also an integer.
// If the parameter is itself not a perfect square then -1 should be returned.
// You may assume the parameter is positive.
// Examples:
// findNextSquare(121) --> returns 144
// findNextSquare(625) --> returns 676
// findNextSquare(114) --> returns -1 since 114 is not a perfect

// function findNextSquare(sq) {
//   let intOfSq = Math.sqrt(sq);
//   if (Number.isInteger(intOfSq)) {
//     let nextInt = intOfSq+1;
//     let nextSq = nextInt*nextInt;
//     return nextSq
//   } else {
//     return -1
//   }
// }

// console.log(findNextSquare(9));


// 25/01/2024
// 8 kyu - Is it a palindrome?
// Write function isPalindrome that checks if a given string (case insensitive)
//  is a palindrome.

// function isPalindrome(x) {
//   let reverse = x.split('').reverse().join('');
//   if (x.toLowerCase() === reverse.toLowerCase()) {
//     return true;
//   } else {
//     return false;
//   }
// }

// console.log(isPalindrome('anna'));

// 26/01/2024
// 7 kyu - Find the middle element
// As a part of this Kata, you need to create a function that when provided with
//  a triplet, returns the index of the numerical element that lies between the
//  other two elements.
// The input to the function will be an array of three distinct numbers
//  (Haskell: a tuple).
// For example:
// gimme([2, 3, 1]) => 0
// 2 is the number that fits between 1 and 3 and the index of 2 in the input
//  array is 0.
// Another example (just to make sure it is clear):
// gimme([5, 10, 14]) => 1
// 10 is the number that fits between 5 and 14 and the index of 10 in the input
// //  array is 1.

// function gimme(inputArray) {
//   let sorted = inputArray.slice().sort((a, b) => a - b);
//   return inputArray.indexOf(sorted[1]);
// }

// console.log(gimme(2, 3, 1));

// // 27/01/2024
// // 8 kyu - Find the smallest integer in the array
// Given an array of integers your solution should find the smallest integer.
// For example:
// Given [34, 15, 88, 2] your solution will return 2
// Given [34, -345, -1, 100] your solution will return -345
// You can assume, for the purpose of this kata, that the supplied array will
//  not be empty.

// class SmallestIntegerFinder {
//   findSmallestInt(args) {
//     return Math.min(...args);
//   }
// }

// 28/01/2024
// 8 kyu - Area or Perimeter
// You are given the length and width of a 4-sided polygon. The polygon can
//  either be a rectangle or a square.
// If it is a square, return its area. If it is a rectangle, return its
//  perimeter.
// area_or_perimeter(6, 10) --> 32
// area_or_perimeter(3, 3) --> 9

// // my code:
// const areaOrPerimeter = function (l, w) {
//   if (l === w) {
//     return l * w;
//   } else {
//     return 2 * (l + w);
//   }
// }

// // best code:
// const areaOrPerimeter = function(l , w) {
//   return l == w ? l*w : 2*(l + w)
// };

// console.log(areaOrPerimeter(3, 3))

// 29/01/2024
// 6 kyu - Find the unique number
// There is an array with some numbers. All numbers are equal except for one.
//  Try to find it!
// findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
// findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
// It’s guaranteed that array contains at least 3 numbers.
// The tests contain some very huge arrays, so think about performance.

// my code:
// function findUniq(arr) {
//   let sorted = arr.sort((a, b) => a - b);
//   if (sorted[0] != sorted[1]) {
//     return sorted[0];
//   } else {
//     return sorted[sorted.length - 1];
//   }
// }

// best code:
// function findUniq(arr) {
//   arr.sort((a,b)=>a-b);
//   return arr[0]==arr[1]?arr.pop():arr[0]
// }

// console.log(findUniq([ 1, 1, 1, 2, 1, 1 ]));

// 30/01/2024
// 7 kyu - The highest profit wins!
// Story
// Ben has a very simple idea to make some profit: he buys something and sells
//  it again. Of course, this wouldn't give him any profit at all if he was
//  simply to buy and sell it at the same price. Instead, he's going to buy it
//  for the lowest possible price and sell it at the highest.
// Task
// Write a function that returns both the minimum and maximum number of the
//  given list/array.
// Examples
// minMax([1,2,3,4,5])   == [1,5]
// minMax([2334454,5])   == [5, 2334454]
// minMax([1])           == [1, 1]
// Remarks
// All arrays or lists will always have at least one element, so you don't
//  need to check the length. Also, your function will always get an array or
//  a list, you don't have to check for null, undefined or similar.

// my code:
// function minMax(arr) {
//   let sorted = arr.sort((a, b) => a - b);
//   return [sorted[0], sorted[sorted.length - 1]];
// }

// // best code:
// // function minMax(arr){
// //   return [Math.min(...arr), Math.max(...arr)];
// // }

// console.log(minMax([2,1,3,4,5]));

// 03/02/2024
// 8 kyu - Grasshopper - Summation
// Summation
// Write a program that finds the summation of every number from 1 to num. The
//  number will always be a positive integer greater than 0.
// For example:
// summation(2) -> 3
// 1 + 2
// summation(8) -> 36
// 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

// my code:
// var summation = function (num) {
//   let sum = 0;
//   for (let i = 1; i <= num; i++) {
//     sum += i;
//   }
//   return sum;
// }

// console.log(summation(36))


// 04/02/2024
// 8 kyu - Exclamation marks series #11: Replace all vowel to exclamation
//  mark in the sentence
// Description:
// Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
// Examples
// replace("Hi!") === "H!!"
// replace("!Hi! Hi!") === "!H!! H!!"
// replace("aeiou") === "!!!!!"
// replace("ABCDE") === "!BCD!"

// // my code:
// function replace(s){
//   return s.replace(/[aeiou]/gi, '!');
// }

// console.log(replace('Hi!'));


// 07/02/2024
// 6 kyu - Create Phone Number
// Write a function that accepts an array of 10 integers (between 0 and 9), that
//  returns a string of those numbers in the form of a phone number.
// Example:
// createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
// The returned format must be correct in order to complete this challenge.
// Don't forget the space after the closing parentheses!


// // // my code:
// function createPhoneNumber(numbers){
//   let format = "(xxx) xxx-xxxx";
//   for (let i = 0; i < numbers.length; i++) {
//     format = format.replace('x', numbers[i]);
//   }
//   return format;
// }

// console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));


// 08/02/2024
// 8 kyu - Beginner - Reduce but Grow
// Given a non-empty array of integers, return the result of multiplying the
//  values together in order. Example:
// [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

// // // my code:
// function grow(x){
//   return x.reduce((a, b) => a * b);
// }

// console.log(grow([1, 2, 3, 4]));

// function sumOfSquares(n){
//   return n.reduce((a, b) => a + b*b);
// }

// console.log(sumOfSquares([1, 2, 3]));


// 10/02/2024
// 8 kyu - If you can't sleep, just count sheep!!
// If you can't sleep, just count sheep!!
// Task:
// Given a non-negative integer, 3 for example, return a string with a murmur:
// "1 sheep...2 sheep...3 sheep..."
// Input will always be valid, i.e. no negative integers.

// // // my code:
// var countSheep = function (num){
//   let murmur = '';
//   for (let i = 1; i <= num; i++) {
//     murmur += i + ' sheep...';
//   }
//   return murmur;
// }

// console.log(countSheep(3));

// 12/02/2024
// 6 kyu - Replace With Alphabet Position
// Welcome.
// In this kata you are required to, given a string, replace every letter with
//  its position in the alphabet.
// If anything in the text isn't a letter, ignore it and don't return it.
// "a" = 1, "b" = 2, etc.
// Example
// alphabetPosition("The sunset sets at twelve o' clock.")
// Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12
// 15 3 11" (as a string)

// // // my code:
// function alphabetPosition(text) {
//   let alphabet = 'abcdefghijklmnopqrstuvwxyz';
//   let position = '';
//   for (let i = 0; i < text.length; i++) {
//     let letter = text[i].toLowerCase();
//     if (alphabet.includes(letter)) {
//       position += alphabet.indexOf(letter) + 1 + ' ';
//     }
//   }
//   return position.trim();
// }
  
// console.log(alphabetPosition('text'));

// 20/02/2024
// 8 kyu - Sentence Smash
// Write a method smash that takes an array of words and smashes them together
//  into a sentence and returns the sentence. You can ignore any need to
//  sanitize words or add punctuation, but you should add spaces between each
//  word. Be careful, there shouldn't be a space at the beginning or the end of
//  the sentence!

// // // my code:
function smash (words) {
  return words.join(' ');
}

console.log(smash(['hello', 'world', 'this', 'is', 'great']));