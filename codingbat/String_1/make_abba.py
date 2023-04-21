'''
Given two strings, a and b, return the result of putting them together in the order abba, 
e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'

'''
#Passing Positional Arguments: Returns the combined string
def make_abba(a, b):
  return a + b + b + a

#Runtime Variables:
def make_abba():

    #Strings declaration and initialization:
    w1 = input("Enter string 1: ")
    w2 = input("Enter string 2: ")

    #Combining two strings:
    final_string = w1 + w2 + w2 + w1

    #Prints the final string:
    print("The 'abba' word is - {} ;)".format(final_string))

make_abba()
