# Your code goes here
vowels = ['a', 'e', 'i', 'o', 'u']
def find_vowels(str):
    string = str.lower()
    vowel_count = 0
    vowels_found = []
    for letter in string:
        if letter in vowels:
            vowels_found.append(letter)
            vowel_count += 1

    return vowel_count, vowels_found

# Test Cases

print(find_vowels("Hello World!"))
print(find_vowels("Uppercase Example"))