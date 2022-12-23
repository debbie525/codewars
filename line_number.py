# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def line_number_list (string):
    line_number_array = []

    for letter in string:
        position = string.index(letter) + 1
        character = letter
        line_number = str(position) +": " + str(character)
        line_number_array.append(line_number)

    return line_number_array

# -----------------------------------------

print(line_number_list("Hello World!"))


