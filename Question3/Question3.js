// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

// Bonus: Can you do this in one pass?


function twoSome(number1, number2, array) {
  const sum = number1 + number2
  console.log(sum)
  console.log(array.indexOf(sum));
  return array.indexOf(number1 + number2) >= 0
}

const myArray = [0, 1, 2, 4, 5]
console.log(twoSome(1,2, myArray))