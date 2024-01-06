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

function simpleMultiplication(number) {
    if (number % 2 == 0) return number * 8;
    else return number * 9;
  }

  console.log(simpleMultiplication(4));

  