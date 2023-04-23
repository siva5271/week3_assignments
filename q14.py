givenString = "HELLO"


def isPalindrome(value):
    for i in range(int(len(value) / 2)):
        if value[i] != value[len(value) - 1 - i]:
            return False
    return True


anonymousFunction = lambda string: isPalindrome(string)

print(anonymousFunction(givenString))
