# Functions go here...
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

# Main routine goes here


how_much = num_check("How much would you like to play with? ", 0, 10)

print("You have chosen to spend ${}.".format(how_much))
# print the
