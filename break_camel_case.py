# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

word = "camelCasing"
new_word=""

for letter in word:
    if letter==letter.upper():
        new_word+=f" {letter}"   
    else:
        new_word+=letter
print(new_word)

