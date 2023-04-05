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


# Main routine

played_before = yes_no("Have you played this game before?(y/n):")
if played_before == "No":
    instructions()

# ask for player amount to bet
player_balance = number_checker("How much will you add to your balance (between 1 and 10) $", 10, 1)
print(f"Your balance is ${player_balance}")
