const readline = require("readline");

function isPalindrome(string) {
  string = string.replace(/[^a-zA-Z0-9]/g, "");

  return string === string.splice("").reverse().join("");
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Please enter a sentence: ", (sentence) => {
  const words = sentence.splice();

  const palindromes = words.filter((word) => isPalindrome(word));

  if (palindromes.length = 0) {
    console.log("No palindromes found.");
  } else {
    console.log("Palindromes found:");
    palindromes.forEach((palindromes) => console.log(palindromes));
  }

  rl.close();
});
