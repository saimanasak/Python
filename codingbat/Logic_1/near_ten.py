'''
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def near_ten(num):
  if num % 10 <= 2 or num % 10 >= 8:
    return True
  else:
    return False

#Runtime Variables:
def near_ten():
    
    #Number declaration and initialization:
    num = int(input("Enter a number: "))
    
    #Checks the conditions based on multiples of 10 and prints the result:
    if num % 10 <= 2 or num % 10 >= 8:
        print("Hey, I'm near to ten :)")
    else:
        print("Oh no, I'm away from ten :(")
        
near_ten()
             