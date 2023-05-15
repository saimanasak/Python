'''
Given a non-empty string and an int n, return a new string 
where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string 
(i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def missing_char(str, n):
  return str[:n] + str[n+1:]

#Runtime Variables:
def missing_char():
    
    #Word and position to be removed: initialization and declaration:
    word = input("Enter a word: ")
    position = int(input("Enter a position of character to be deleted: "))
    
    #The final word after removing the character:
    final_word = word[:position] + word[position+1:]
    
    #Prints the final word:
    print(f"Missed character word: {final_word}")
    
missing_char()
