display_instructions = ""
while display_instructions.lower() != "xxx":

    # Ask the user if they have played before
    display_instructions = input("Have you played before? ").lower()

    # If they say 'yes', output 'program continues'
    if display_instructions == "yes" or display_instructions == "y":
        display_instructions = "yes"
        print("Program continues")

    # If they say 'no', output 'display instructions'
    elif display_instructions == "no" or display_instructions == "n":
        display_instructions = "no"
        print("Display instructions")

    # If "xxx" is entered, end
    elif display_instructions == "xxx":
        print("Program ends")
        break

    # If they don't respond with either yes or no, print error msg

    else:
        print("Please answer 'yes' or 'no'")
