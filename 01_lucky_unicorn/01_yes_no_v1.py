# Ask the user if they have played before
display_instructions = input("Have you played before? ").lower()

# If they say 'yes', output 'program continues'
if display_instructions == "yes":
    print("You selected 'yes'")
    print("Program continues")

# If they say 'no', output 'display instructions'
elif display_instructions == "no":
    print("You selected 'no'")
    print("Display instructions")

# If they don't respond with either yes or no

else:
    print("Please answer 'yes' or 'no'")
    