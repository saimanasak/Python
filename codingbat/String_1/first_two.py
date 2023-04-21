'''
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" 
yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'

'''
#Passing Positional Arguments: Returns the first two characters of a string
def first_two(str):
  return str[0:2]

#Runtime Variables:
def first_two():

    #String declaration and initialization:
    word = input("Enter a word: ")
    out = len(word)

    #Condition to check the length of the string:
    while(out < 2):
        print("Please, enter a word which has more than 2 characters :)")
        word = input("Enter a word: ")
        out = len(word)

    #First two characters of a string:
    o_word = word[0:2]
    
    #Prints the first two characters of a string:
    print("The first 2 characters are: {}".format(o_word))

first_two()
