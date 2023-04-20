'''
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
The string length will be at least 2.

'''

def extra_end():

    word = input("Enter a word: ")
    out = len(word)

    end_str = word[-2::]

    final_word = end_str + end_str + end_str

    print(end_str)
    print("Expected word: {}".format(final_word))

extra_end()