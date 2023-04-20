"""
Given two strings, a and b, return the result of putting them together in the order abba, 
e.g. "Hi" and "Bye" returns "HiByeByeHi".

"""


def make_abba():

    w1 = input("Enter string 1: ")
    w2 = input("Enter string 2: ")

    final_string = w1 + w2 + w2 + w1

    print("The 'abba' word is - {} ;)".format(final_string))

make_abba()