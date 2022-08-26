# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

a = [1, 2,2]
b = [1]

def array_diff(a, b):
    b_duplicate=[]
   
    for number in b:
        if number in a:
            a.remove(number)
            b_duplicate.append(number)
    for number in b_duplicate:
        b.remove(number)
            
    final_array =[]
    for number in a:
        final_array.append(number)
    for number in b:
        final_array.append(number)
        
    return final_array


print(array_diff(a,b))