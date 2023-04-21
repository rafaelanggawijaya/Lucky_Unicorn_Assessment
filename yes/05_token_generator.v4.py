"""Component 3 Token Generator v4
 Generates random tokens (Unicorn, Zebra, Horse, Donkey)
 Update: percentages are changed
        unicorns come out 5%
        zebra come out 32.5%
        horse come out 32.5%
        donkey come out 30%
of the time.
Also changed code so it is easier to test.
 created by Rafael Anggawijaya"""

# imports random function
import random


# Balance for test

STARTING_BALANCE = 100
balance = STARTING_BALANCE
# test loop for generating random tokens

for item in range(20):
    number = random.randint(1, 100)
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
    print(f"Token:{token} current balance:{balance}")

# output
print(f"\nStarting balance:${STARTING_BALANCE:.2f}")
print(f"Ending balance:${balance:.2f}")
