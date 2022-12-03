# Write a function that takes a single string (word) as argument. 
# The function must return an ordered list containing the indexes of 
# all capital letters in the string.

# capitals('CodEWaRs'), [0,3,4,6]

def capital(word):
    index = 0
    index_list =[]
    for letter in word:
        if letter == letter.upper():
            index_list.append(index)    
        index+=1
    return index_list

#----------------------------------------------------------------

print(capital("CodEWaRs"))

