# Your code goes here
def is_palindrome(string):
    if len(string) < 2:
        return print(False)

    l, r = 0, len(string) - 1

    while l < r:
        if string[l] != string[r]:
            return print(False)
        l += 1
        r -= 1

    return print(True)


def substring(string):
    for letter in range(len(string)):
        for i in range(letter + 1, len(string) + 1):
            if is_palindrome(string[letter:i]):
                print(string[letter:i])
                


# Test Cases
string = 'YCBAABCY'
string1 = 'YCBAZBCY'
string2 = 'A'

substring(string)
substring(string1)
substring(string2)
