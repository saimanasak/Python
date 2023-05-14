'''
Given three ints, a b c, return True if one of b or c is "close" 
(differing from a by at most 1), while the other is "far", 
differing from both other values by 2 or more. 
Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def close_far(a, b, c):
  if abs(a - b) <= 1:
    if abs(a - c) >= 2 and abs(b - c) >= 2:
      return True
    else:
      return False
  elif abs(a - c) <= 1:
    if abs(a - b) >= 2 and abs(b - c) >= 2:
      return True
    else:
      return False
  else:
    return False

#Runtime Variables:
def close_far():
    
    #3 numbers' initialization and declaration:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    #Checks the conditions based on values and prints the result:
    if abs(a - b) <= 1:
        if abs(a - c) >= 2 and abs(b - c) >= 2:
            print("All the values are close and far.")
        else:
            print("All the values aren't close and far.")
    elif abs(a - c) <= 1:
        if abs(a - b) >= 2 and abs(b - c) >= 2:
            print("All the values are close and far.")
        else:
            print("All the values aren't close and far.")
    else:
        print("All the values aren't close and far.")
        
close_far()
