"""Component 3 Token Generator v1
 Generates random tokens (Unicorn, Zebra, Horse, Donkey
 created by Rafael Anggawijaya"""

# imports random function
import random

tokens = ["unicorn", "zebra", "horse", "donkey"]

# test loop for generating random tokens

for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # easier to screenshot
