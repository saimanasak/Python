'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def string_splosion(str):
  final_str = ""
  for i in range(len(str)):
    final_str += str[:i+1]  
  return final_str

#Runtime Variables:
def string_splosion():
    
    #Word and empty string initialization and declaration:
    word = input("Enter a word: ")
    final_string = ""
    
    #Length of the word:
    length = len(word)
    
    #Adds a character to the previous characters for each iteration:
    for i in range(length):
        final_string = final_string + word[:i+1]
    
    #Prints the final word:
    print(f"Word after splosion: {final_string} ")
    
string_splosion()
