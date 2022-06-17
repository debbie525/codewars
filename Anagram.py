# An anagram is the result of rearranging the letters of a word to produce a new word
# example: below ==> elbow


def is_anagram(test, original):
    sorted_test = sorted(test)
    sorted_original = sorted (original)

    if len(sorted_test)!=len(sorted_original):
        return False

    for item in range (0, len(sorted_test)-1):
        if sorted_test[item]!= sorted_original[item]:
            return False
    return True

print(is_anagram("bad girl", "girl dab"))