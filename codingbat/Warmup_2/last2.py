'''
Given a string, return the count of the number of times 
that a substring length 2 appears in the string and also as 
the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def last2(str):
  c=0
  length = len(str)
  if length < 2:
    return 0
  for i in range(length-2):
    if str[i:i+2] == str[-2:]:
      c+=1
  return c

#Runtime Variables:
def last2():
    
    #Word and count initialization and declaration:
    word = input("Enter a word: ")
    count = 0
    
    #Length of the word:
    length = len(word)
    
    #Checks if word length is less than 2:
    if length < 2:
        print("Too small word.")
    
    #Iterates till the length, except the last 2 characters:
    for i in range(length-2):
        if word[i:i+2] == word[-2:]:
            count = count + 1
    
    #Prints the final count:
    print(f"Count: {count}")
    
last2()
    