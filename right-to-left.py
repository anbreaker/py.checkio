import unittest

# "For centuries, left-handers have suffered unfair discrimination
#  in a world designed for right-handers."
# Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.

# "Most humans (say 70 percent to 95 percent) are right-handed,
# a minority (say 5 percent to 30 percent) are left-handed, and an
# indeterminate number of people are probably best described as ambidextrous."
# Scientific American. www.scientificamerican.com

# One of the robots is charged with a simple task: to join a sequence
# of strings into one sentence to produce instructions on how to get around
# the ship. But this robot is left-handed and has a tendency to joke around
# and confuse its right-handed friends.

# You are given a sequence of strings. You should join these strings into chunk
# of text where the initial strings are separated by commas. As a joke on the
# right handed robots, you should replace all cases of the words "right" with
# the word "left", even if it's a part of another word. All strings are given
# in lowercase.

# Input: A sequence of strings as a tuple of strings (unicode).

# Output: The text as a string.

# Example:

# left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# left_join(("bright aright", "ok")) == "bleft aleft,ok"
# left_join(("brightness wright",)) == "bleftness wleft"
# left_join(("enough", "jokes")) == "enough,jokes"


def left_join(phrases):
    """
        Join strings and replace "right" to "left"
        tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
        str =  ''.join(tup)
        print(str)

    """
    phrasesNew = ','.join(phrases)
    phrasesNew = phrasesNew.replace('right', 'left')

    return phrasesNew


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")
                     ) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")
                     ) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")
                     ) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
