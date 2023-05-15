'''
Given 2 strings, a and b, return the number of the positions
where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" 
substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def string_match(a, b):
  c=0
  for i in range(len(a)-1):
    if a[i:i+2] == b[i:i+2]:
      c+=1
  return c
    
#Runtime Variables:
def string_match():
    
    #Words and count initialization and declaration:
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    count = 0
    
    #Minimum length of 2 words:
    length = min(len(word1), len(word2))
    
    #Iterates to the full length of the word:
    for i in range(length-1):
        if word1[i:i+2] == word2[i:i+2]:
            count = count + 1
    
    #Prints the final count:
    print(f"Count: {count}")

string_match()
