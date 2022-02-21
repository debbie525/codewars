# Create a function that when provided with a triplet, 
# returns the index of the numerical element that lies between the other two elements.
# The input to the function will be an array of three distinct numbers.

# For example:

# gimme([2, 3, 1]) => 0
# 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

# Another example (just to make sure it is clear):

# gimme([5, 10, 14]) => 1
# 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.


def gimme(input_array):
    sorted_input_array = sorted(input_array)    # sort in ascending order
    middle = sorted_input_array[1]              # get the middle element
    answer = input_array.index(middle)          # get the index of middle element from original array
    print(answer)


gimme([5,30,20])