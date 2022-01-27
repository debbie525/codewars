# Complete the solution so that the function will break up camel casing, using a space between words.

# Example:
# "camelCasing"  =>  "camel Casing"

def solution(word):
    new_word = ""
    for letter in word:
    
        if letter.isupper() == True:
            new_word += " " + letter
        else:
            new_word +=letter
            
    print(new_word)

# ----------------------------------------

solution("camelCasing")