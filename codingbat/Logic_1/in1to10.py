'''
Given a number n, return True if n is in the range 1..10, inclusive. 
Unless outside_mode is True, in which case return True 
if the number is less or equal to 1, or greater or equal to 10.

in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def in1to10(n, outside_mode):
  if outside_mode == True:
    if n <= 1 or n >= 10:
      return True
    else:
      return False
  else:
    if n >= 1 and n <= 10:
      return True
    else:
      return False

#Runtime Variables:
def in1to10():
    
    #Number and mode initialization and declaration:
    num = int(input("Enter a number: "))
    outside_mode = input("Is it in outside_mode??? (y or n) ")
    
    #Checks the conditions based on the mode and returns the value:
    if outside_mode == 'y':
        if num <= 1 or num >= 10:
            print("In the range.... :)")
        else:
            print("Outside the range.... :(")
    else:
        if num >= 1 and num <= 10:
            print("In the range.... :")
        else:
            print("Outside the range.... :(")
            
in1to10()
