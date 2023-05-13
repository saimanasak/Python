'''
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, 
it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def lone_sum(a, b, c):
  if a == b == c:
    return 0
  elif a == b:
    return c
  elif b == c:
    return a
  elif c == a:
    return b
  else:
    return a + b + c

#Runtime Variables:
def lone_sum():
    
    #3 numbers' initialization and declaration:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    #Sum of the 3 numbers:
    sum = a + b + c
    
    #Checks the conditions based on numbers and prints the sum:
    if a == b == c:
        print("Lone sum value: 0")
    elif a == b:
        print(f"Lone sum value: {c}")
    elif b == c:
        print(f"Lone sum value: {a}")
    elif c == a:
        print(f"Lone sum value: {b}")
    else:
        print(f"Lone sum value: {sum}")
        
lone_sum()
