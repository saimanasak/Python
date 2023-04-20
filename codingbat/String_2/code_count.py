'''
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

'''
import re
def code_count():

    word = input("Enter the code word: ")

    c = re.findall("co.?e", word)

    print("List: {}".format(c))

    print("Count: {}".format(len(c)))

code_count()