# Write a function that takes in a string of one or more words, 
# and returns the same string, but with all five or more letter words 
# reversed (Just like the name of this Kata). Strings passed in will 
# consist of only letters and spaces. Spaces will be included only when 
# more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"


def reversed_words(sentence):
    sentence_list = sentence.split(" ")
    for item in sentence_list:
        
        if len(item)>=5:
            new_item=""
            position=-1

            for letter in item:
                new_item+=(item[position])                      # append the letters in reverse position
                position+=-1

            sentence_list[sentence_list.index(item)]=new_item   # update the list with reversed word(new_item)
         
    new_sentence=""
    for word in sentence_list:
        new_sentence+=word +" "                                 # create a new sentence with reversed words
    return new_sentence.rstrip()                                # rstrip- removes the space in the right

# ---------------------------------------------------------------------------------------------------------

print(reversed_words("Hey fellow warriors"))
print(reversed_words("This is a test"))
print(reversed_words("This is another test"))

