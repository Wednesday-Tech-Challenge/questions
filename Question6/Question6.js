// Your code goes here

//function for palindrome
function palindrome(str) {
// bring letters to lowercase
let lowerString = str.toLowerCase()

//compare words forward and backwards
let strReverse = lowerString.split('').reverse().join('')
console.log(strReverse)

return strReverse === lowerString
}
// Test Cases


console.log(palindrome("Racecar"))