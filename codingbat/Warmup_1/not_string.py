'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def not_string(str):
  if not str.startswith("not"):
    return 'not ' + str
  else:
    return str

#Runtime Variables:
def not_string():
    
    #Word initialization and declaration:
    word = input("Enter a word: ")
    
    #Checks for the condition based on "not" and prints the not_word:
    if not word.startswith("not"):
        not_string = "not " + word
        print(f"The 'not' word is: {not_string}")
    else:
        print(f"The not word is: {word}")
    
not_string()
