# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([1, 1, 1, 2, 1, 1]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

def find_unique_num(num_list):
    compare = num_list[0]           # this is the 1st number in the array
    num_list.remove(num_list[0])    # remove the 1st number in array
    same_number_counter=0

    for number in num_list:
        if number==compare:
            same_number_counter+=1

    if same_number_counter==0:
        return compare
    elif same_number_counter>0:
        for number in num_list:
            if number!=compare:
                return number

# --------------------------------------------

print(find_unique_num([1, 1, 1, 10, 1, 1]))
print(find_unique_num([0, 0, 0.55, 0, 0]))

    


