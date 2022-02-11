# You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. 
# You may assume the parameter is non-negative.

# Examples:(Input --> Output)
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square

from math import sqrt


def find_next_square(input):
    answer = sqrt(input)
    next_perfect_square = False

    if answer.is_integer():
        while next_perfect_square is False:
            input +=1
            next_answer = sqrt(input)
            if next_answer.is_integer():
                next_perfect_square = True        
        print(f"Next perfect square: {input}")
    else:
        print("The input is not a perfect square")

# -------------------------------------------------------
user_input = int(input("Please type a perfect square number: "))
find_next_square(user_input)