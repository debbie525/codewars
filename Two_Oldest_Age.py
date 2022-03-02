# The two oldest ages function/method needs to be completed. 
# It should take an array of numbers as its argument and return the two highest numbers within the array. 
# The returned value should be an array in the format [second oldest age, oldest age].
# The order of the numbers passed in could be any order. 
# The array will always include at least 2 items. If there are two or more oldest age, 
# then return both of them in array format.

# For example:
# two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]

def two_oldest_age(ages):
    sorted_input = sorted(ages)    # sort the list in ascending order
    oldest = sorted_input[-1]      # last item is the highest number
    for item in range (1, (len(ages))):
        if len(ages)==2:
            return sorted_input
        elif sorted_input[-item] == oldest:
            continue
        else:
            second_oldest = sorted_input[-item]
            break                             # oldest and second oldest already known, break the loop
            
    for item in ages:
        if item== oldest or item == second_oldest:
            continue
        else:
            sorted_input.remove(item)        # items except oldest and second oldest will be removed
            

    return sorted_input
    

print(two_oldest_age([10, 1]))


