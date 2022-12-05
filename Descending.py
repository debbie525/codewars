''''
Descending Order

Your task is to make a function that can take any non-negative integer 
as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.

'''

def sorted_integer(num):

    num_list = []
    for item in str(num):
        num_list.append(int(item))

    descend_list=sorted(num_list, reverse=True)

    final_output = ''
    for item in descend_list:
        final_output += str(item)
    return final_output

print(sorted_integer(8899822754403519))

#-------------------------------------------------------------

def sorted_integer_2(num):
    num_list = []

    for element in str(num):
        num_list.append(int(element))

    descend_list =[num_list[0]]
    num_list.remove(num_list[0])

    for number in num_list:
        if number in descend_list:
            descend_list.insert(((descend_list.index(number))+1), number)

        elif number<descend_list[0] and number>descend_list[-1]:
            for item in reversed(descend_list) :
                if number < item:
                    if descend_list.count(item)>1:
                        descend_list.insert((descend_list.index(item)+descend_list.count(item)), number)
                    else:
                        descend_list.insert((descend_list.index(item)+1), number)
                    break

        elif number > descend_list[0]:
            descend_list.insert(0, number)
            
        elif number < descend_list[-1]:
            descend_list.append(number)

    final_output=""
    for item in descend_list:
        final_output+=str(item)

    return final_output
            
print(sorted_integer_2(8899822754403519))   


