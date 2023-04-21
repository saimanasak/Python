'''
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'

'''
#Passing Positional Arguments: Returns the combination of 3 copies of the last two characters of the string
def extra_end(str):
  end_str = str[-2::]
  return end_str + end_str + end_str

#Runtime Variables:
def extra_end():

    #String declaration and initialization:
    word = input("Enter a word: ")

    #Condition to get the last two characters of a string:
    end_str = word[-2::]

    #3 copies of the last two characters:
    final_word = end_str + end_str + end_str

    #Prints the expected word:
    print(end_str)
    print("Expected word: {}".format(final_word))

extra_end()
