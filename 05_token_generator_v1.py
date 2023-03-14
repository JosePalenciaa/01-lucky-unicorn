import random

# main routine goes here...

tokens = ["Unicorn", "Horse", "Zebra", "Donkey"]

# testing loop to generate 20 tokens
for item in range(0,21):
    chosen = random.choice(tokens)
    print(chosen, end='\t')
