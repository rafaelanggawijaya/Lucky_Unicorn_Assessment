"""Lucky Unicorn project
A game of luck where the player bets money. Depending on what they
get they can lose or gain money.
Update: added token generator function
by Rafael Anggawijaya"""

import random


# yes/no function

def yes_no(question_text):
    while True:
        # ask player input - (if they have played the game before)

        answer = input(question_text).lower()

        # if player input == yes or y output - (Game Starting)

        if answer == "y" or answer == "yes":
            answer = "yes"
            return answer

        # if player input == no or n output - ('instructions')
        elif answer == "n" or answer == "no":
            answer = "no"
            return answer

        # otherwise output - (error)
        else:
            print("error -invalid input- (please enter yes/no or y/n)")


# instruction function

def instructions():
    print("***How To Play***")
    print()
    print("The rules of the game go here")
    print()


# number checking function
def number_checker(question, high, low):
    error = "<error> -invalid input- " \
            "Please enter a number between {} and {}\n".format(high, low)

    # Loop to ask player for a valid input

    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check if amount meets requirements
            if 0 < response <= 10:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# token generator function
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


# Main routine

played_before = yes_no("Have you played this game before?(y/n):")
if played_before == "no":
    instructions()

# ask for player amount to bet
player_balance = number_checker("How much will you add to your balance (between 1 and 10) $", 10, 1)
print(f"Your balance is ${player_balance}")
ending_balance = token_generator(player_balance)
print(f"\nThank you for playing\nYour starting balance was ${player_balance}\n You ended with ${ending_balance}")
