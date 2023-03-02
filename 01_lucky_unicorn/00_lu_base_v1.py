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
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
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


# Main routine goes here...
played_before = yes_no("Have you played Lucky Unicorn before? ")

if played_before == "no":
    instructions()

print()

# Asks user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You have chosen to spend ${}.".format(how_much))
