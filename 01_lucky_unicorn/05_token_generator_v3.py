import random

# main routine goes here...

tokens = ["unicorn", "horse", "zebra", "donkey"]
starting_balance = 100

balance = starting_balance
# testing loop to generate 100 tokens
for item in range(0, 100):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4

    elif chosen == "horse" or "zebra":
        balance -= 0.5

    else:
        balance -= 0.5

# output
print()
print("Starting balance: ${:.2f}".format(starting_balance))
print("Final Balance: ${:.2f}".format(balance))
