'''
The number 6 is a truly great number. 
Given two int values, a and b, return True if either one is 6. 
Or if their sum or difference is 6. 
Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def love6(a, b):
    
  if a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6:
    return True
  else:
    return False

#Runtime Variables:
def love6():
    
    #Two integer's initialization and declaration:
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    
    #Operations on the two numbers:
    sum = a + b
    difference = abs(a - b)
    
    #Checks based on the conditions and prints:
    if a == 6 or b == 6 or sum == 6 or difference == 6:
        print("We love 6")
    else:
        print("We love all other numbers")
        
love6()
