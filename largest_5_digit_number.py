# In the following 6 digit number:

# 283910
# 91 is the greatest sequence of 2 consecutive digits.

# In the following 10 digit number:

# 1234567890
# 67890 is the greatest sequence of 5 consecutive digits.

# Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. 
# The number will be passed in as a string of only digits. It should return a five digit integer. 
# The number passed may be as large as 1000 digits.

input_digits = 39296789
comparison_number =0
input_digits_list =[]
for item in str(input_digits):
        input_digits_list.append(item)


for count in range(1, len(str(input_digits))+1):
    if len(input_digits_list)>=5:
        new_number =""
        for item in range (0,5):
            new_number+=input_digits_list[item]
        print(f"New number: {new_number}")

        if int(new_number)>int(comparison_number):
            comparison_number=new_number
        input_digits_list.remove(input_digits_list[0])
   
        

print(comparison_number)
       
    

















