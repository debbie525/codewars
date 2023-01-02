# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89

# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089

# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string


def ip_validation(ip_address):

    ip_address_list = ip_address.split(".")         # convert string to array/list

    if len(ip_address_list)!= 4:
        return False
    else:
        for item in ip_address_list:
            if len(item)>3:
                return False
            elif item.isnumeric()==False:
                return False
            elif len(item)>1 and item[0]=="0":      # check if octet with more than 1 digit has leading zero
                return False
            elif int(item)>255 or int(item)<0:
                return False

        return True

# ---------------------------------------------------------------
print(ip_validation(ip_address="12.255.56.1"))      # answer: True
print(ip_validation(ip_address=""))                 # answer: False / no element
print(ip_validation(ip_address="abc.def.ghi.jkl"))  # answer: False / not numeric
print(ip_validation(ip_address="123.456.789.0"))    # answer: False / second octet exceeds 255
print(ip_validation(ip_address="12.34.56"))         # answer: False / three octets only
print(ip_validation(ip_address="12.34.56 .1"))      # answer: False / third octet has " " string character
print(ip_validation(ip_address="12.34.56.-1"))      # answer: False / fourth octet is a negative number
print(ip_validation(ip_address="123.045.067.089"))  # answer: False / second, third and fourth octet has leading zeros
print(ip_validation(ip_address="127.1.1.0"))        # answer: True
print(ip_validation(ip_address="0.0.0.0"))          # answer: True
print(ip_validation(ip_address="0.34.82.53"))       # answer: True
print(ip_validation(ip_address="192.168.1.300"))    # answer: False / fourth octet is greater than 255
 



