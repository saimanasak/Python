'''
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

'''
def first_half():

    word = input("Enter a word: ")
    length = int((len(word) / 2))
    
    final_word = word[0:length]

    print("The first half is: {}".format(final_word))

first_half()