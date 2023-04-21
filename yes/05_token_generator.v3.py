"""Component 3 Token Generator v3
 Generates random tokens (Unicorn, Zebra, Horse, Donkey
 Update: previous code had the house lose most of the time
        unicorns come out 10%
        zebra come out 20%
        horse come out 20%
        donkey come out 50%
of the time
 created by Rafael Anggawijaya"""

# imports random function
import random

tokens = ["unicorn", "zebra", "zebra", "horse", "horse", "donkey", "donkey", "donkey", "donkey", "donkey", ]

# Balance for test

STARTING_BALANCE = 100
balance = STARTING_BALANCE
# test loop for generating random tokens

for item in range(20):
    token = random.choice(tokens)

    # changes balance

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.5
    print(f"Token:{token} current balance:{balance}")

# output
print(f"\nStarting balance:${STARTING_BALANCE:.2f}")
print(f"balance:${balance:.2f}")
