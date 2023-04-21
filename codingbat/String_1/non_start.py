'''
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'

'''
#Passing Positional Arguments: Returns the combined word by remvoing the first characters from the 2 strings.
def non_start(a, b):
  return a[1::] + b[1::]

#Runtime Variables:
def non_start():

    #Strings declaration and initialization:
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    #Eliminates the first character from the two strings and combines:
    final_word = word1[1::] + word2[1::]

    #Prints the combined word:
    print("Incomplete word: {}".format(final_word))

non_start()
