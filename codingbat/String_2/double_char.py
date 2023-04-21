'''
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

'''
#Passing Positional Arguments: Returns the copy of each character in the string
def double_char(str):
    double = ""
    for w in str:
      double = double + w * 2
    return double

#Runtime Variables:
def double_char():

    #String declaration and initialization:
    word = input("Enter a word: ")
    double = ""
    
    #Copies the each character from the given string and prints the final string:
    for w in word:
        double = double + w * 2
    print("Doubled word is: {}".format(double))

double_char()
