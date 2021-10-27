'''
Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

Examples:

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

'''

def reverse_string():
    string = input('Please input a string:')        
    string_list = []
    
    for item in string.split():
        string_list.append(item)
        string_list.append(' ')
   

    print('Original String: ' + string)

    new_string = ''
    for item in string_list:
        n = -1
        for j in range(len(item)):
            new_string += item[n]
            n += -1
    print('Reversed String: ' + new_string.strip())

# Call the function
reverse_string()

    