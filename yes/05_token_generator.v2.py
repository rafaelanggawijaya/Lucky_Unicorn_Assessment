"""Component 3 Token Generator v2
 Generates random tokens (Unicorn, Zebra, Horse, Donkey
 Update: change code to test if the house wins
 created by Rafael Anggawijaya"""

# imports random function
import random

tokens = ["unicorn", "zebra", "horse", "donkey"]

# Balance for test

balance = 100

# test loop for generating random tokens

for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # easier to screenshot

    # changes balance

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # output
    print(f"Token:{token} Your balance:${balance}")