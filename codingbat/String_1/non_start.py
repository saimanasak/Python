'''
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

'''

def non_start():

    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    final_word = word1[1::] + word2[1::]

    print("Incomplete word: {}".format(final_word))

non_start()