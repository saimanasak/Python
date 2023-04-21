'''
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

'''
#Passing Positional Arguments: Returns the value based on the given conditions.
def end_other(a, b): 
  a1 = a.lower()
  b1 = b.lower()
  if a1.endswith(b1) or b1.endswith(a1):
    return True
  else:
    return False

#Runtime Variables:
def end_other():

    #Strings declaration and initialization:
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    #Converts the both strings into lower case:
    a = word1.lower()
    b = word2.lower()

    #Checks if both the strings end with same string and prints the result:
    if a.endswith(b) or b.endswith(a):
        print("Hey! they have same ends :)")
    else:
        print("Oops! they have different ends :(")
    
end_other()
