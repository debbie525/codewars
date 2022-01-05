'''
Find the prime factors of a given number

Prime numbers are numbers that have only 2 factors: 1 and themselves 

'''

number = int(input("Enter a number to factor (positive integer only): "))

factor_list =[]

for factor in range(2,number):  # not included in items to check: 1 and the number itself
    if number%factor==0:
        factor_list.append(factor)
    else:
        continue

if len(factor_list) == 0:
    print (f"{number} is a prime number.")
else:
    print(f"The prime factors of {number} are {factor_list}.")