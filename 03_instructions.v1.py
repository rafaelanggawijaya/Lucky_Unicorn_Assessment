"""Took function from 02_yes_no.checker_function.v1.py which is needed with the instruction function to make this
section."""


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
    print("Game starting")
    print()


# Main routine

played_before = yes_no("Have you played this game before?(y/n):")
if played_before == "No":
    instructions()
else:
    print("game starting")
