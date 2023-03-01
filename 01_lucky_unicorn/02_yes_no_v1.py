# Functions go at the top of the code (above main routine)
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

# Main routine goes here...


display_instructions = yes_no("Have you played before? ")

print("You chose {}".format(display_instructions))
