
# Write a function to determine if a given string is a palindrome
# Palindrome - a word, phrase, or sequence other sequence of characters which reads the same backward as forward
# example: madam, level, racecar



def check_palindrome_1(word):
    word_list = []
    for letter in word:
        word_list.append(letter)

    reverse =list(reversed(word_list))

    if word_list == reverse:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")


def check_palindrome_2(word):
    reverse_word = ""
    for number in range(1,len(word)+1):
        print(number)
        reverse_word += word[-(number)]
    if word == reverse_word:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
    


check_palindrome_2(word="racecar")

