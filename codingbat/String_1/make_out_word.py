'''
Given an "out" string length 4, such as "<<>>", and a word, 
return a new string where the word is in the middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'

'''
#Passing Positional Arguments: Returns the final maked out word (places the string in between the special braces)
def make_out_word(out, word):
  n_out = len(out)
  f_out1 = int(n_out / 2)
  c1 = out[0:f_out1]
  f_out2 = (-f_out1)
  c2 = out[f_out2::]
  return c1 + word + c2

#Runtime Variables:
def make_out_word():

    #Strings declaration and initialization:
    out = input("Enter the output string, should be of special braces: ")
    word = input("Enter the word: ")

    #Places the string in between the given special braces:
    n_out = int((len(out))/2)
    c1 = out[0:n_out]
    c2 = out[-(n_out)::]

    #Prints the final maked out word:
    print("The maked out word is {}{}{}".format(c1,word,c2))

make_out_word()
