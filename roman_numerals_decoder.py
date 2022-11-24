# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
# You don't need to validate the form of the Roman numeral.

# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, 
# starting with the leftmost digit and skipping any 0s. 
# So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). 
# The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

# Example:

# solution('XXI') # should return 21
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def decimal_to_roman(decimal):
    roman_conversion = {"M":1000,"CM":900, "D":500,"CD":400,"C":100,"XC":90, 
                        "L":50, "XL":40, "X":10, "IX":9, "V":5,"IV":4, "I":1}
    converted_numeral=""
    
    for key, value in roman_conversion.items():
        multiplier = int(decimal/value)
        if multiplier >=1:
            for i in range (multiplier):
                converted_numeral+=key
            excess_number = decimal - (value * multiplier)
            decimal= excess_number

    return converted_numeral

def roman_to_decimal(roman_numeral):
    roman_conversion = {"M":1000,"CM":900, "D":500,"CD":400,"C":100,"XC":90, 
                        "L":50, "XL":40, "X":10, "IX":9, "V":5,"IV":4, "I":1}
    decimal =[]
    index_1 = 0
    index_2 = 1

    for key, value in roman_conversion.items():
        for i in range (roman_numeral.count(key)):
            if len(key)==1 and key in roman_numeral[index_1:(index_2)]:
                decimal.append(roman_conversion[key])
                index_1+=1
                index_2+=1 
            
            elif len(key)==2 and key in roman_numeral[index_1:(index_2+1)]:
                decimal.append(roman_conversion[key])
                index_1+=2
                index_2+=2   
            
    return(sum(decimal))

# ------------------------------------------------------------------------------

print(f"Decimal to Roman Numeral: {decimal_to_roman(1666)}")
print(f'Roman Numeral to Decimal: {roman_to_decimal("MDCLXVI")}')



        

