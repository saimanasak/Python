'''
Given a string, return a new string made of every other char starting with the first, 
so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def string_bits(str): 
  str1 = ""
  for i in range(0, len(str)):
    if i % 2 == 0:
      str1 = str1 + str[i]
  return str1

#Runtime Variables:
def string_bits():
    
    #Word initialization and declaration:
    word = input("Enter a word: ")
    
    #Length of the given string and empty string:
    length = len(word)
    final_word = ""
    
    #Checks the conditions and prints the string with even position characters:
    for i in range(0, length):
        if i % 2 == 0:
            final_word = final_word + word[i]

    #Prints the final word:
    print(f"Final word: {final_word}")
    
string_bits()
