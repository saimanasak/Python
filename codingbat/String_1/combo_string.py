'''
Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).

'''

def combo_string():
     
     word1 = input("Enter first word: ")
     word2 = input("Enter second word: ")

     len1 = len(word1)
     len2 = len(word2)

     if(len1 > len2):
          final1 = word2 + word1 + word2
          print("Combined string is: {}".format(final1))
     elif(len1 < len2):
          final2 = word1 + word2 + word1
          print("Combined string is: {}".format(final2))

combo_string()