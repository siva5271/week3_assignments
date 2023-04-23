givenString="MALAYALAM"

def isPalindrome(value):
    for i in range(int(len(value)/2)):
        if(value[i]!=value[len(value)-1-i]):
            return False
    return True

flag=isPalindrome(givenString)
if flag:
    print("The string is a palindrome!")
else:
    print("The given string is not a palindrome!")