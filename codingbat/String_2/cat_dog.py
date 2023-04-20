'''
Return True if the string "cat" and "dog" appear in the given string.

'''

import re
def cat_dog():

    word = input("Enter a word: ")

    if re.search('cat', word) and re.search('dog', word):
        print("True!!!")
    else:
        print("False!!!")

cat_dog() 