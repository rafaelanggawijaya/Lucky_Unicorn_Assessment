"""Component 4 -rounds- v3
Same as component 3 (token generator)
Changed: turned program to a function
By Rafael Anggawijaya"""

import random


def token_generator(balance):
    rounds_play = 0

    for item in range(20):
        rounds_play += 1
        number = random.randint(1, 100)  # makes it so only donkeys can be chosen
        if number <= 5:
            token = "unicorn"
        elif number <= 35:
            token = "donkey"
        else:
            if number % 2 == 0:
                token = "zebra"
            else:
                token = "horse"

        # changes balance

        if token == "unicorn":
            balance += 4
        elif token == "donkey":
            balance -= 1
        else:
            balance -= 0.5
        # output
        print(f"Round: {rounds_play}. Token: {token}.  current balance: ${balance}")
        if balance == 0:
            print("Sorry you have no more money")
            break
        enter = input("Do you want to continue?(Enter Key for yes, X to end):").upper()
        if enter == "X":
            break
    return balance


# main routine
starting_balance = 5
ending_balance = token_generator(starting_balance)
print(f"\nThank you for playing\nYour starting balance was ${starting_balance}\n You ended with ${ending_balance}")
