'''
Given two int values, return their sum. 
Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b

#Passing Positional Arguments:
def sum_double():
    
    #2 numbers' initialization and declaration:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    #Sum of the two numbers:
    sum = a + b
    
    #Checks the conditions and prints either the doubled sum or just sum:
    if a == b:
        value = sum * 2
        print(f"Doubled sum value: {value}")
    else:
        print(f"Sum: {sum}")
        
sum_double()
