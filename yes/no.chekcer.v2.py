""" Lucky Unicorn project -Yes/No-
 Confirmation for player if they have played the game before,
 player input can either be y or n if not prints out error
 Update: Added feature that players can now input yes and no
 project by Rafael Anggawijaya
 """
# ask player input - (if they have played the game before)

question_player = input("Have you played this game before?(y/n):").lower()

# if player input == yes or y output - (Game Starting)
if question_player == "y" or question_player == "yes":
    print("Game Starting")

# if player input == no or n output - ('instructions')
elif question_player == "n" or question_player == "no":
    print("Instructions")

# otherwise output - (error)
else:
    print("error -invalid input- (please enter yes/no or y/n)")

