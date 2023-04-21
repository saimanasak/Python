'''
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

'''
#Passing Positional Arguments: Returns the first half part of the string
def first_half(str):
    length = int((len(str) / 2))
    return str[0:length]

#Runtime Variables:
def first_half():

    #String declaration and initialization:
    word = input("Enter a word: ")
    
    #Half string:
    length = int((len(word) / 2))
    final_word = word[0:length]
    
    #Prints the first half of the string:
    print("The first half is: {}".format(final_word))

first_half()
