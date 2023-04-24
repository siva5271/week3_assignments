import json

pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chillipowder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chillipowder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

def pantryUpdate(dish):
    for x in dish:
        pantry[x]=pantry[x]-1
    displayPantry()
    
def displayPantry():
    print("Available pantry:")
    for x in pantry:
        print(x, ":", pantry[x])

selection = int(
    input(
        "Enter 1 for butter chicken\nEnter 2 for chicken and chips\nEnter 3 for pizzza\nEnter 4 for sandwich\nEnter 5 for beans on toast\nSpam a la tin"
    )
)
match selection:
    case 1:
        pantryUpdate(recipes["Butter chicken"])
    case 2:
        pantryUpdate(recipes["Chicken and chips"])
    case 3:
        pantryUpdate(recipes["Pizza"])
    case 4:
        pantryUpdate(recipes["Egg sandwich"])
    case 5:
        pantryUpdate(recipes["Beans on toast"])
    case 6:
        pantryUpdate(recipes["Spam a la tin"])
    case __:
        print("Enter a valid input!")
