# Create a function that will square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, 
# because 9**2 is 81 and 1**2 is 1.
# Note: The function accepts an integer and returns an integer


def square_digits(digits):

    new_digits = ""

    for number in str(digits):
        square_num = int(number)**2
        new_digits+=str(square_num)
        
    return(int(new_digits))

#----------------------------------------------

print(square_digits(9119))