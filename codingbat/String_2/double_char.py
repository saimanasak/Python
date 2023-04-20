'''
Given a string, return a string where for every char in the original, there are two chars.

'''
def double_char():

    word = input("Enter a word: ")
    double = ""
    
    for w in word:
        double = double + w * 2
    print("Doubled word is: {}".format(double))

double_char()
