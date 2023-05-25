def is_palindrome(string):
    # Remove whitespace and non-alphanumeric characters
    string = ''.join(filter(str.isalnum, string)).lower()

    # Check if string is equal to its reverse
    return string == string[::-1]


# Prompt user for input sentence
while True:
    sentence = input("Please enter a sentence: ")
    if sentence:
        break
    print("Error: Please enter a non-empty sentence.")

# Split sentence into words
words = sentence.split()

# Check each word for palindromes
palindromes = []
for word in words:
    if is_palindrome(word):
        palindromes.append(word)

# Print results
if not palindromes:
    print("No palindromes found.")
else:
    print("Palindromes found:")
    for palindrome in palindromes:
        print(palindrome)
