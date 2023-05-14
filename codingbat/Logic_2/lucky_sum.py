'''
Given 3 int values, a b c, return their sum. 
However, if one of the values is 13 then it does not count towards the sum 
and values to its right do not count. 
So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  else:
    return a + b + c


#Runtime Variables:
def lucky_sum():
    
    #3 numbers' initialization and declaration:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    #Checks for value 13 and prints the sum:
    if a == 13:
        print("Lucky sum value: 0")
    elif b == 13:
        print(f"Lucky sum value: {a}")
    elif c == 13:
        print(f"Lucky sum value: {a+b}")
    else:
        print(f"Lucky sum value: {a+b+c}")
        
lucky_sum()
    