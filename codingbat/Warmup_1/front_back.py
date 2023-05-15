'''
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def front_back(str):
  length = len(str)
  if length <= 1:
    return str
  else:
    half_word = str[1:length-1]
    return str[length-1] + half_word + str[0]

#Runtime Variables:
def front_back():
    
    #Word initialization and declaration:
    word = input("Enter a word: ")
    
    #Calculates the length of the string:
    length = len(word)
    
    #Checks the conditions and prints:
    if length <= 1:
        print(f"Reversed word: {word}")
    else:
        half_word = word[1:length-1]
        final_word = word[length-1] + half_word + word[0]
        print(f"Reversed word: {final_word}")

front_back()
