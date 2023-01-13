# Create a function that converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always 
# capitalized.

# Examples:
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"



def to_camel_case(string):
    new_string=""

    if "-" in string or "_" in string:
        temp_string=string.replace("_", "-")
        string_list = temp_string.split("-")

    else:
        return ""

    for word in string_list:
        if word==string_list[0]:
            new_string+=word
        else:
            capitalized_word = word.title()
            new_string+=capitalized_word

    return new_string

# ------------------------------------------------------------

#string = "the-stealth-warrior"
#string = "The_Stealth_Warrior"
string ="The_Cat-was_Hungry"

print(to_camel_case(string))