# Create a function that takes a list of non-negative integers 
# and strings and returns a new list with the strings filtered out.

raw_list = [0.1, 1, 2, 3, "a", "b", 1.2]


def integer_only(raw_list):
        integer_only = []
        for item in raw_list:
                if isinstance(item, int) == True:
                        integer_only.append(item)
        return integer_only

print(integer_only(raw_list))