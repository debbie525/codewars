# Your task, is to create N×N multiplication table, of size provided in parameter.
# For example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:

# [[1,2,3],[2,4,6],[3,6,9]]

def multiplication_table(size):

    sub_list=[]
    container_list =[]
    final_list =[]

    for item in range(1, size +1):
        sub_list.append(item)                            # create the 1st layer of multiplication table

    for multiplier in range( 1, size+1):
        for number in sub_list:
            container_list.append(number*multiplier)     # multiply the 1st layer to create the next layer/size
        final_list.append(container_list)                # append the layer of  multiplication table
        container_list=[]                                # initialize/empty the list before the next loop

    return final_list

# ----------------------------------------------------------------------

print(multiplication_table(size=3))
print(multiplication_table(size=4))
print(multiplication_table(size=5))

