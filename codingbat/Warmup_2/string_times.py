'''
Given a string and a non-negative int n,
return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def string_times(str, n):
  return str * n

#Runtime Variables:
def string_times():
    
    #Word and Times: initialization and declaration:
    word = input("Enter a word: ")
    times = int(input("Enter no.of times to be repeated: "))
    
    #Repeated word based on no.of times:
    repeated_word = word * times
    
    #Print the repeated word:
    print(f"Repeared word: {repeated_word}")
    
string_times()
