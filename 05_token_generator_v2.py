import random

# main routine goes here...

tokens = ["Unicorn", "Horse", "Zebra", "Donkey"]
balance = 100

# testing loop to generate 20 tokens
for item in range(0,20):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "Unicorn":
        balance += 4

    elif chosen == "Horse" or "Zebra":
        balance -= 0.5

    else:
        balance -= 0.5

    # output
    print("Token: {}, Balance: ${}.".format(chosen, balance))