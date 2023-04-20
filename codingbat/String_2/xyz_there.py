'''
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.

'''
import re
def xyz_there():

    word = input("Enter a xyz word: ")

    if re.findall(r"\Bxyz", word):
        print("True!!!")
    else:
        print("False!!!")

xyz_there()
    