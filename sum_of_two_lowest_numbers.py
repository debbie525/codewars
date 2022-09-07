# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
# No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.



numbers = [19, 5, 42, 2, 77]
sorted_numbers=[]

for i in range(len(numbers)):
    max_number= 0
    for item in numbers:
        if item > max_number:
            max_number=item

    sorted_numbers.insert(0, max_number)
    numbers.remove(max_number)

sum= sorted_numbers[0] + sorted_numbers[1]
print(f"Sorted Numbers: {sorted_numbers}")
print(f"Sum of two lowest numbers: {sum}")

