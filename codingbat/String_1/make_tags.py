'''
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'

'''
#Passing Positional Arguments: Returns the final tagged string.
def make_tags(tag, word):
  tagged_string = "<" + tag + ">" + word + "</" + tag + ">"
  return tagged_string

#Runtime Variables:
def make_tags():
    
    #Strings declaration and initialization:
    tag = input("Enter tag: ")
    word = input("Enter the word to be tagged: ")

    #Prints the final tagged word:
    print("The final tagged word is <{}> {} </{}>".format(tag, word, tag))

make_tags()
