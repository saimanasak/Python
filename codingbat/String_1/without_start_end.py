'''
Given a string, return a version without the first and last char, so "Hello" yields "ell". 
The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'

'''
#Passing Positional Arguments: Returns the string by removing the first and last characters of the string.
def without_end(str):
    return str[1:((len(str)) - 1)]

#Runtime Variables:
def without_start_end():

    #String declaration and initialization:
    word = input("Enter a word: ")

    #Prints the word without the first and last characters from the given word:
    print("Word without head and tail is: {} ;)".format(word[1:(len(word)-1)]))

without_start_end()
