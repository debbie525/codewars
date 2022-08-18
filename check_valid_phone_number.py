# Write a function that accepts a string, and returns true if it is in the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)

# Examples:

# "(123) 456-7890"  => true
# "(1111)555 2345"  => false
# "(098) 123 4567"  => false


phone_number = "(098) 123-1567"

def check_number(phone_number):
    number_to_check = ["0", "1", "2", "3", "4", "5", "6","7","8","9"]
    if phone_number[0]=="(" and phone_number[4]==")" and phone_number[5] ==" " and phone_number[9]=="-":
        for item in range (1, 14 ):
            if item==4 or item == 5 or item ==9:
                continue
            elif phone_number[item] not in number_to_check:
                return False
                          
    else:
        return False

    return True

print(check_number(phone_number))





