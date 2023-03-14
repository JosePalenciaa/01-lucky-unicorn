def statement_generator(statement, decoration, above_below):
    sides = decoration * 3

    # statement = "{} {} {}".format(sides, statement, sides)
    statement = f"{sides} {statement} {sides}"
    top_bottom = above_below * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# main routine goes here
statement_generator("Welcome to Lucky Unicorn", "*", "-")
print()
