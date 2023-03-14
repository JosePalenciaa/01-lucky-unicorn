import random


# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If they say 'yes', output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If they say 'no', output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer 'yes' or 'no'")


def instructions():

    print()
    statement_generator("HOW TO PLAY", "!", "-")
    print()
    print("Choose a starting amount (minimum of $1, maximum of $10).")
    print("Then press < ENTER > to play. You will get either a hor-\nse, "
          "zebra, a donkey, or unicorn.")
    print()
    print("It costs $1 per round. Depending on your prize, you might\nwin "
          "some of the money back. Here's the payout amounts...")
    print("Unicorn: $5.00 (balance increases by $4")
    print("Donkey: $0.00 (balance decreases by $1")
    print("Horse / Zebra: $0.50 (balance decreases by $0.50")

    return ""


def num_check(question, low, high):
    error = "Please enter a whole number from 1 to 10. \n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high...
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


def statement_generator(statement, decoration, above_below):
    sides = decoration * 3

    # statement = "{} {} {}".format(sides, statement, sides)
    statement = f"{sides} {statement} {sides}"
    top_bottom = above_below * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here...
statement_generator("Welcome to Lucky Unicorn", "*", "*")
played_before = yes_no("Have you played Lucky Unicorn before? ")

if played_before == "no":
    instructions()

print()

# Asks user how much they want to play with...
statement_generator("Let's get started", "!", "=")
how_much = num_check("How much would you like to play with? ", 0, 10)
print("You have chosen to spend ${}".format(how_much))

balance = how_much

rounds_played = 0

print()
play_again = input("Press < Enter > to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    statement_generator("Round: {}".format(rounds_played), "-", "-")
    print()

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

    statement_generator("You got a {}. Your balance is: {:.2f}".format(chosen, balance), "!", "!")

    if balance < 1:
        play_again = 'xxx'
        print("Sorry, you have ran out of money")

    else:
        play_again = input("Press <Enter> to play again, or 'xxx' to quit: ")

    if play_again == 'xxx':
        break

print()
statement_generator("RESULTS", "=", "=")
print()
print("Starting amount: ${:.2f}".format(how_much))
print("Final balance: ${:.2f}".format(balance))
print("Thank you for playing Lucky Unicorn!")
