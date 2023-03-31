""" Lucky Unicorn project -Yes/No_function-v1
 Confirmation for player if they have played the game before,
 player input can either be y or n if not prints out error.
 Feature: Now the program is a function and can be used in any other code
 project by Rafael Anggawijaya
 """


# Function

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


# Main routine

question = yes_no("Have you played this game before?(y/n):")
print(f"You have entered {question}")
