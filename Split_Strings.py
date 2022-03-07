# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing 
# second character of the final pair with an underscore ('_').

# Examples:
# 'abc' =>  ['ab', 'c_']
# 'abcdef' => ['ab', 'cd', 'ef']


def split_string(input_string):
    string_set =""
    splitted_string =[]
    count=0
    for item in input_string:
        count+=1
        string_set+=item
        if len(string_set)==2:
            splitted_string.append(string_set)
            string_set=""             # re-initialize the value

        # if length of input string is odd and iteration at last item
        if len(input_string)%2!=0 and count ==len(input_string):
            string_set = input_string[-1] + "_"  # last character plus "_"
            splitted_string.append(string_set)

    return splitted_string

print(split_string("abc"))
print(split_string("abcdef"))
print(split_string("asdfadsf"))
print(split_string("asdfads"))
print(split_string(""))

