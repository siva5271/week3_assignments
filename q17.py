first=int(input("Enter the first number"))
second=int(input("Enter the second number"))
selection = int(
    input(
        "Enter a number:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division"
    )
)
match selection:
    case 1:
        print("Result:",(first+second))
    case 2:
        print("Result:"(first-second))
    case 3:
        print("Result:",(first*second))
    case 4:
        print("Result:",(first/second))