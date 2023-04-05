""" Component 2 How much v1
Asks player how much money they want to bet (Between 1 and 10 and has to be a whole number)
This input goes to their account balance which is what they would use to play and withdraw from
project by Rafael Anggawijaya"""

# asks for player bet amount

player_bet = int(input("How much money do you want to enter?(1<= and >= 10) $"))

# Setting player balance

player_balance = 0

# checking if player input is valid

while not 1 <= player_bet <= 10:
    print("error -invalid input- Please enter a whole number between 1 and 10 ")
    # asks for input again
    player_bet = int(input("How much money do you want to enter?(1<= and >= 10 $"))

player_balance += player_bet
print(f"You will be playing with ${player_balance}")
