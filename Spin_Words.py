# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only 
# when more than one word is present.

# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
#           spinWords( "This is a test") => returns "This is a test" 
#           spinWords( "This is another test" )=> returns "This is rehtona test"
# Note: words with less than 5 characters will not be reversed

def spin_words(sentence):
    sentence_list = sentence.split(' ')
    spin_words = ""

    for word in sentence_list:
        new_word = ""
        for item in range (1, len(word)+1):
            new_word += word[-(item)]    # reverse the word

        if len(word)>5:
            spin_words += (" " + new_word)
        else:
            spin_words += (" " + word)

    print(spin_words.strip()) # use strip to remove trailing spaces

spin_words("Hey fellow warriors")





