'''
Return True if the string "cat" and "dog" appear in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

'''
#By importing the "re" regular expression:
#Runtime Variables:
import re
def cat_dog():

    #String declaration and initialization:
    word = input("Enter a word: ")

    #Searches for the cat and dog and prints either True or False:
    if re.search('cat', word) and re.search('dog', word):
        print("True!!!")
    else:
        print("False!!!")

cat_dog() 
