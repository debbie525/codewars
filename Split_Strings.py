# Create a funtion that will split a string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing 
# second character of the final pair with an underscore ('_').

# Examples:

#  'abc' =>  ['ab', 'c_']
#  'abcdef' => ['ab', 'cd', 'ef']

def split_into_pair(string):
    new_string = []
    new_char =''

    for i in range(len(string)):
        new_char+=string[i]
        if len(new_char)==2:                    
            new_string.append(new_char)         # append two characters in new array
            new_char =''                        # reset/empty the new_char

    if len(string)%2!=0:                        # check if the length of string is odd                    
        new_char+="_"                           # add "_" to the remaining 1 character
        new_string.append(new_char)
    
    return new_string

#--------------------------------------------------------------------
print(split_into_pair("abc"))
print(split_into_pair("abcdef"))
print(split_into_pair("asdfadsf"))
print(split_into_pair(""))
print(split_into_pair("a"))

        

