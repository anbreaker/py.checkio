# In this mission you should check if all elements in the given list are equal.

# Input: List.

# Output: Bool.

# Example:

# all_the_same([1, 1, 1]) == True
# all_the_same([1, 2, 1]) == False
# all_the_same(['a', 'a', 'a']) == True
# all_the_same([]) == True

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here

    elementsSet = set(elements)

    if len(elementsSet) == 1 or len(elementsSet) == 0:
        return True
    else:
        return False

    # return (element[1:]==element[:-1])


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
