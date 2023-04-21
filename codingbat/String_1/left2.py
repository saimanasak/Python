'''
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'

'''
#Passing Positional Arguments: Returns the left rotated word
def left2(str):
  return str[2::] + str[0:2]

#Runtime Variables:
def left2():

    #String declaration and initialization:
    word = input("Enter a word: ")

    #Rotate left the two characters:
    final_word = word[2::] + word[0:2]

    #Prints the left rotated string:
    print("Left rotated string is: {}".format(final_word))

left2()
