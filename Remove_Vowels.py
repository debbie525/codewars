# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
# neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def remove_vowels(string):
    new_string = ""
    vowel_list = ["a", "e", "i", "o", "u"]
    for character in string:
        if character in vowel_list:
            continue
        else:
            new_string += character

    print(new_string)


remove_vowels("Happy Birthday 123 to you")