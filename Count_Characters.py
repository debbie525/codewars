
# Count characters in your string
# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.


def count_char(input_string):
    new_dict = {}                               # create an empty dictionary
    for item in input_string:
        new_dict[item] = input_string.count(item)   # add a key, value pairs in dict

    print(new_dict)

count_char("debbie")