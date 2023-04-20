'''
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
The string length will be at least 2.

'''
def left2():

    word = input("Enter a word: ")

    final_word = word[2::] + word[0:2]

    print("Left rotated string is: {}".format(final_word))

left2()