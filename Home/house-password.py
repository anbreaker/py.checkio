def checkio(data: str) -> bool:
    oneNumber = 0
    oneUpperCase = 0
    oneLowerCase = 0
    if data.isalnum() and len(data) >= 10:  # The password contains only ASCII latin letters or digits
        for d in data:                      # Greater than or equal to 10 symbols
            if d.isdigit():                 # it has at least one digit
                oneNumber = 1
            if d.isupper() == True:         # as well as containing one uppercase letter
                oneUpperCase = 1
            if d.islower() == True:         # one lowercase letter in it
                oneLowerCase = 1

        if oneNumber == 1 and oneUpperCase == 1 and oneLowerCase == 1:
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
