# Write a function that takes an integer as input, and returns the number of bits that are equal to 
# one in the binary representation of that number. 
# You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this
#Tip:
# How to convert a decimal to binary:
# 1. Divide the given decimal number by 2 and note down the remainder.
# 2. Now, divide the obtained quotient by 2, and note the remainder again.
# 3. Repeat the above steps until you get 0 as the quotient.
# 4. Now, write the remainders in such a way that the last remainder is written first, 
# followed by the rest in the reverse order.
# 5. This can also be understood in another way which states that Least Significant Bit (LSB) 
# of the binary number is at the top and the Most Significant Bit (MSB) is at the bottom. 
# This number is the binary value of the given decimal number.

input_integer = int(input("Please provide the integer:"))

binary_output = []
quotient = 1

while quotient!=0:
    remainder = input_integer%2
    quotient = int(input_integer/2)
    binary_output.insert(0, remainder)  # insert th remainder at index 0
    # print(f"Remainder: {remainder}")
    # print(f"quotient: {quotient}")
    input_integer = quotient

print(binary_output)
print(f"bits: {binary_output.count(1)}")