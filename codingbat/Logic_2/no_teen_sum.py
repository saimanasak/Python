'''
Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in the range 13..19 inclusive -- 
then that value counts as 0, except 15 and 16 do not count as a teens.
Write a separate helper "def fix_teen(n):"that takes in an int value 
and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
Define the helper below and at the same indent level as the main no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def no_teen_sum(a, b, c):
  def fix_teen(n):
    if n in [13,14,17,18,19]:
      return 0
    else:
      return n
    
  a1 = fix_teen(a)
  b1 = fix_teen(b)
  c1 = fix_teen(c)
    
  return a1 + b1 + c1

#Runtime Variables:
def no_teen_sum():
    
    #3 numbers' initialization and declaration:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    #Helper function: returns the value by checking the conditions.
    def fix_teen(n):
        if n >= 13 and n <= 19 and n != 15 and n != 16:
            return 0
        else:
            return n
    
    #Assigns the values to their respective new variables:
    a1 = fix_teen(a)
    b1 = fix_teen(b)
    c1 = fix_teen(c)
    
    #Prints the sum of final values:
    print(a1+b1+c1)
    
no_teen_sum()
    