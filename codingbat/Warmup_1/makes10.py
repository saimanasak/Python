'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def makes10(a, b):
  if a == 10 or b == 10 or a+b ==10:
    return True
  else:
    return False

#Runtime Variables:
def makes10():
    
    #Two numbers' initialization and declaration:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    #Checks the conditions for 10 and prints:
    if a == 10 or b == 10 or a + b == 10:
        print("10s in the numbers!!")
    else:
        print("No 10s in the numbers.")
        
makes10()
