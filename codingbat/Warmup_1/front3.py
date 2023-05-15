'''
Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def front3(str):
  return str[:3] + str[:3] + str[:3]

#Runtime Variables:
def front3():
    
    #Word initialization and declaration:
    word = input("Enter a word: ")
    
    #3 copies of first 3 characters of word:
    copy_word = word[:3] + word[:3] + word[:3]
    
    #Prints the final word:
    print(f"Copied word: {copy_word}")
    
front3()
