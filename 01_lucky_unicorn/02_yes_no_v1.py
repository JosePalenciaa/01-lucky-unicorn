# Functions go at the top of the code (above main routine)
def yes_no(question):
    valid = False
    while not valid:
            response = input("Have you played before? ").lower()

            # Main goes here...
            # If they say 'yes', output 'program continues'
            if response == "yes" or response == "y":
                    response = "yes"
                    print("Program continues")

            # If they say 'no', output 'display instructions'
            elif response == "no" or response == "n":
                    response = "no"
                    print("Display instructions")

            # If they don't respond with either yes or no, print error msg

            else:
                print("Please answer 'yes' or 'no'")
