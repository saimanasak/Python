'''
Given a string, return a version without the first and last char, so "Hello" yields "ell". 
The string length will be at least 2.

'''
def without_start_end():

    word = input("Enter a word: ")
    #length = (len(word)) - 1

    print("Word without head and tail is: {} ;)".format(word[1:(len(word)-1)]))

without_start_end()