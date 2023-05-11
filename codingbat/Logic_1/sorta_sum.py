'''
Given 2 ints, a and b, return their sum. 
However, sums in the range 10..19 inclusive, are forbidden, 
so in that case just return 20.

sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def sorta_sum(a, b):
  sum = a + b
  if (sum >= 10 and sum <= 19):
    return 20
  else:
    return sum

#Runtime Variables:
def sorta_sum():
    
    #Two integer's initialization and declaration:
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    
    #Sum of the two integers:
    sum = a + b
    
    #Checks the conditions and prints the sum value:
    if (sum >= 10 and sum <= 19):
        print("20")
    else:
        print(sum)
    
sorta_sum()
