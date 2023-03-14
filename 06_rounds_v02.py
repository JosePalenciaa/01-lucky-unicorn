import random
# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press < Enter > to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("Round: #{}".format(rounds_played))

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
            balance -= 0.5
        else:
            chosen = "zebra"
            balance -= 0.5

    print("You got a {}. Your balance is: {:.2f}".format(chosen, balance))

    if balance == 0:
        play_again = 'xxx'
        print("Sorry, you have ran out of money")

    else:
        play_again = input("Press <Enter> to play again, or 'xxx' to quit: ")

print()
print("Final balance: ${}".format(balance))
