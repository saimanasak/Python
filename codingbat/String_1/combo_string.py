'''
Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'

'''
#Passing Positional Arguments: Returns the combined string
def combo_string(a, b):
     len1 = len(a)
     len2 = len(b)
     if(len1 > len2):
          return b + a + b      
     elif(len1 < len2):
          return a + b + a

#Runtime Variables:    
def combo_string():
     
     #Strings declaration and initialization:
     word1 = input("Enter first word: ")
     word2 = input("Enter second word: ")

     #Lengths of the two strings:
     len1 = len(word1)
     len2 = len(word2)

     #Checks for the big word between the two strings and prints the combined string:
     if(len1 > len2):
          final1 = word2 + word1 + word2
          print("Combined string is: {}".format(final1))
     elif(len1 < len2):
          final2 = word1 + word2 + word1
          print("Combined string is: {}".format(final2))

combo_string()
