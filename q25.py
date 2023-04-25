class EnterOneException(Exception):
    # Exception raised when input is one
    pass

userSelection=int(input("Enter any number except 1:"))
try:
    if(userSelection==1):
        raise EnterOneException
    else:
        print("No exception found")
except EnterOneException:
    print("Exception raised!")