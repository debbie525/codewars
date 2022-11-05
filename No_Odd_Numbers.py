# Write a small function that returns the values of an array that are not odd.

# All values in the array will be integers. Return the good values in the order they are given.

values = [1,3,2,5,67,89,10]



def no_odds(values):
    even_numbers_only=[]
    for number in values:
        if number % 2 ==0:
            even_numbers_only.append(number)
    return even_numbers_only

print(no_odds(values))