'''
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, 
then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def pos_neg(a, b, negative):
  if (negative == True and a < 0 and b < 0) or (negative == False and ((a < 0 and b >= 0) or (b < 0 and a >= 0))):
    return True
  else:
    return False

#Runtime Variables:
def pos_neg():
    
    #Numbers and Negative initialization and declaration:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    negative = input("Is it negative??? (y or n) ")
    
    #Checks the conditions and prints the status of the numbers:
    if (negative == "y" and a < 0 and b < 0) or (negative == "n" and ((a < 0 and b >= 0) or (b < 0 and a >= 0))):
        print("Numbers are negative.")
    else:
        print("Numbers aren't negative.")
pos_neg()
