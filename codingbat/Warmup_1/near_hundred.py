'''
Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def near_hundred(n):
  if abs(n - 100) <= 10 or abs(n - 200) <= 10:
    return True
  else:
    return False

#Runtime Variables:
def near_hundred():
    
    #Number initialization and declaration:
    n = int(input("Enter a number: "))
    
    #Checks the conditions and prints whether the number is near to 100 or 200:
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        print("Number is near to 100 or 200")
    else:
        print("Number isn't near to 100s")
        
near_hundred()
