'''
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2 

'''
#By importing "re" regular expression:
#Runtime Variables:
import re
def code_count():

    #String declaration and initialization:
    word = input("Enter the code word: ")

    #Checks for the given regular expression and prints:
    c = re.findall("co.?e", word)
    print("List: {}".format(c))
    print("Count: {}".format(len(c)))

code_count()
