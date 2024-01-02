// 02/01/2024
// Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

function smash (words) {
    return words.join(' ')
};

let words = ['hello', 'world', 'this', 'is', 'great']
console.log(smash(words)) // returns "hello world this is great"