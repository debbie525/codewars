# You are going to be given a word. Your job is to return the middle character of the word.
#  If the word's length is odd, return the middle character. If the word's length is even, 
# return the middle 2 characters.

# #Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"




def get_middle(word):
    if len(word)%2==0:
        index_1 = int((len(word)/2)-1)      # python index starts at 0, need to decrease by 1
        index_2 = int((len(word)/2))
        middle = word[index_1] + word[index_2]
    
    else:
        index=int(len(word)//2)             # floor division
        middle = word[index]

    print(middle)

get_middle("debbie")