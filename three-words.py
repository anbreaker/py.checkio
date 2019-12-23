import unittest

# Let's teach the Robots to distinguish words and numbers.

# You are given a string with words and numbers separated by
# whitespaces (one space). The words countains only letters.
# You should check if the string countains three words in succession.
# For example, the string "start 5 one two three 7 end"
# countains three words in succession.

# Input: A string with words.

# Output: The answer as a boolean.

# Example:

# checkio("Hello World hello") == True
# checkio("He is 123 man") == False
# checkio("1 2 3 4") == False
# checkio("bla bla bla bla") == True
# checkio("Hi") == False


def checkio(words: str) -> bool:
    words = words.split(' ')
    count = 0
    for w in words:
        if w.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    else:
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("hola") == False, "hola"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete, cool rewards!")
