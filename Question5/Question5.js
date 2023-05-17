/// Your code goes here

function find_vowels(str) {
const vowels = ["a", "e", "i", "o", "u"]
let vowel_count = 0
let vowel_array = []
str = str.toLowerCase();


// loop over each letter in the string and add any vowel to vowel_array & vowel_count ++
for (let i = 0; i < str.length; i++) {
    const new_i = str[i];
}

if (vowels.includes(new_i)) {
    vowel_count++;
}

if (!vowel_array.includes(new_i)) {
    find_vowels.push(new_i)
}
}

/// Test Cases

console.log(vowel_array("momentum"))
console.log(vowel_count)
