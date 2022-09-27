# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

string = "Dermatoglyphics"
unique_chars = []

def is_isogram(string):
    unique_chars =[]
    for letter in string.lower():
        if letter not in unique_chars:
            unique_chars.append(letter)
        else:
            return False


    return True

print(is_isogram(string))