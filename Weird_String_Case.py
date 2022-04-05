# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string 
# with all even indexed characters in each word upper cased, and all odd indexed characters in each word 
# lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that 
# character should be upper cased and you need to start over for each word.

# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only 
# be present if there are multiple words. Words will be separated by a single space(' ').
# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'


def weird_string_case(string):
    new_string = ""
    index=0

    for character in string:
        if character ==" ":
            index = -1
            new_string+=character
        else:
            if index%2 == 0:
                new_string+=character.upper()
            else:
                new_string+=character.lower()
        index+=1

    return new_string  


# --------------------------------------------

print(weird_string_case("hello world"))