'''
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

'''
#Passing Positional Arguments:
def xyz_there(str):
  return str.count("xyz") != str.count(".xyz")

#By importing "re" regular expression:
#Runtime Variables:
import re
def xyz_there():

    #String declaration and initialization:
    word = input("Enter a xyz word: ")

    #Checks for the given regular expression and prints the result:
    if re.findall(r"\Bxyz", word):
        print("Hey! there's is 'xyz' in the given string :)")
    else:
        print("Oops! there's no 'xyz' in the string :(")

xyz_there()
    