# In the following 10 digit number:

# 1234567890
# 67890 is the greatest sequence of 5 consecutive digits.

# Complete the solution so that it returns the greatest sequence of five consecutive 
# digits found within the number given. 
# The number will be passed in as a string of only digits. It should return a five digit integer. 
# The number passed may be as large as 1000 digits.

def largest_5digits(number):
    number_list=[]

    for item in number:
        number_list.append(item)   # create a number array/list

    start_position = 0
    end_position = 5
    max_number = 0
    join_number = ""
    last_index= len(number_list) + 1


    while last_index != end_position:
        number = int(join_number.join(number_list[start_position:end_position]))
        if number > max_number:
            max_number=number
        start_position+=1
        end_position+=1

    return max_number

# -----------------------------------------------------------------
number ="1234567890"
print(f"The largest 5 digist numbr is: {largest_5digits(number)}")





    




