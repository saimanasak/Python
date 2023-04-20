'''
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.

'''
def end_other():

    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    a = word1.lower()
    b = word2.lower()

    if a.endswith(b) or b.endswith(a):
        print("True!!!")
    else:
        print("False!!!")
    
end_other()