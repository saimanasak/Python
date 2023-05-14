'''
Given an int n, return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def diff21(n):
  if n > 21:
    return (abs(n - 21) * 2)
  else:
    return abs(n - 21)

#Runtime Variables:
def diff21():
    
    #Number initialization and declaration:
    n = int(input("Enter a number: "))
    
    #Absolute difference of number and 21:
    diff = abs(n - 21)
    
    #Checks the conditions and prints either the absolute doubled difference or just difference:
    if n > 21:
        d_diff = diff * 2
        print(f"Absolute doubled difference: {d_diff}")
    else:
        print(f"Absolute difference: {diff}")
        
diff21()
