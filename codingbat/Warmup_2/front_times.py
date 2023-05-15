'''
Given a string and a non-negative int n, 
we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. 
Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def front_times(str, n):
   return str[:3] * n

#Runtime Variables:
def front_times():
    
    #Word and Times: initialization and declaration:
    word = input("Enter a word: ")
    times = int(input("Enter no.of times to be repeated: "))
    
    #Repeated word of first 3 characters based on no.of times:
    copied_word = word[:3] * times
    
    #Prints the final word:
    print(f"Copied word: {copied_word}")
    
front_times()
