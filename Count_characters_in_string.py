# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count_occurrence(string):
    new_dict={}                                #create an empty dictionary

    for item in string:
        counter = string.count(item)
        new_dict.update({item:counter})        # update the key, value pair of dictionary

    return new_dict

#---------------------------------------------------
print(count_occurrence("aba"))
print(count_occurrence(""))
print(count_occurrence("characters"))