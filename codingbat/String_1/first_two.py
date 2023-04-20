'''
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" 
yields the empty string "".

'''

def first_two():

    word = input("Enter a word: ")
    out = len(word)

    while(out < 2):
        print("Please, enter a word which has more than 2 characters :)")
        word = input("Enter a word: ")
        out = len(word)

    o_word = word[0:2]
    print("The first 2 characters are: {}".format(o_word))

first_two()