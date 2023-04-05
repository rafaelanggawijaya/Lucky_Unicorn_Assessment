""" Component 2 How much v2
Asks player how much money they want to bet (Between 1 and 10 and has to be a whole number)
This input goes to their account balance which is what they would use to play and withdraw from
Changed: redid program to add strings to the loop when given and invalid input
project by Rafael Anggawijaya"""

error = "Please enter a whole number between 1 and 10\n"
valid = False

# Loop to ask player for a valid input

while not valid:
    try:
        # ask for amount
        user_balance = int(input("How much do you want to play with? (1<= amount >= 10) $"))

        # check if amount meets requirements
        if 0 < user_balance <= 10:
            print(f"You are going to play with ${user_balance}")
            valid = True

        else:
            print("error -invalid input- Please enter a whole number between 1 and 10")

    except ValueError:
        print("error -invalid input- Please enter a whole number between 1 and 10")

