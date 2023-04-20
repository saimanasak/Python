'''
Given an "out" string length 4, such as "<<>>", and a word, 
return a new string where the word is in the middle of the out string, e.g. "<<word>>".

'''

def make_out_word():

    out = input("Enter the output string, should be of special braces: ")
    word = input("Enter the word: ")

    n_out = int((len(out))/2)
    c1 = out[0:n_out]
    c2 = out[-(n_out)::]

    print("The maked out word is {}{}{}".format(c1,word,c2))

make_out_word()