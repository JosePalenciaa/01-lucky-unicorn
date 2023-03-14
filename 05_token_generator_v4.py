import random

# main routine goes here...

starting_balance = 100

balance = starting_balance
# testing loop to generate < amount > tokens
for item in range(0, 10):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # User gets unicorn (+4) of # between 1 and 5
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # User has 30% chance to get donkey (-1)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # 32.5% chance for either horse or zebra (-0.5)
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
            balance -= 0.5

    print("You got {}. Your balance is: {:.2f}".format(chosen, balance))

# output
print()
print("Starting balance: ${:.2f}".format(starting_balance))
print("Final Balance: ${:.2f}".format(balance))
