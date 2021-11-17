'''
Python program to display the fibonacci sequence up to n-th term

Example:

n=13
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

'''

try:
    n = int(input('Please enter the number of terms:'))

    num1 = 0
    num2 = 1

    counter = 0
    print('Fibonacci Sequence:')
    while counter < n:
        print(num1)
        answer = num1 + num2
        # update the values
        num1 = num2
        num2 = answer
        counter += 1

except ValueError:
    print('Invalid input, please enter a positive integer')

