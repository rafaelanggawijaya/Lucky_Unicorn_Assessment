""" Component 2 How much v3
Asks player how much money they want to bet (Between 1 and 10 and has to be a whole number)
This input goes to their account balance which is what they would use to play and withdraw from
Change: Turned program to a function so that it can be reused for other programs
project by Rafael Anggawijaya"""


# function

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


# main routine

player_balance = number_checker("How much will you add to your balance (between 1 and 10) $", 10, 1)
print(f"Your balance is ${player_balance}")
