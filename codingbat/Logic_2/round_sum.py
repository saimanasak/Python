'''
For this problem, we'll round an int value up to the next multiple of 10 
if its rightmost digit is 5 or more, so 15 rounds up to 20. 
Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5,
so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. 
To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
Write the helper entirely below and at the same indent level as round_sum().

round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def round_sum(a, b, c):
  def round10(n):
    rem = n % 10
    if rem >= 5:
      n1 = n - rem
      return n1 + 10
    else:
      return n - rem
    
  a1 = round10(a)
  b1 = round10(b)
  c1 = round10(c)
    
  return a1 + b1 + c1

#Runtime Variables:
def round_sum():
    
    #3 numbers' initialization and declaration:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    #Rounds each number to multiple of 10 and returns:
    def round10(n):
        rem = n % 10
        if rem >= 5:
            n1 = n - rem
            return n1 + 10
        else:
            return n - rem
    
    #Assigns the rounded values to their respective new values:
    a1 = round10(a)
    b1 = round10(b)
    c1 = round10(c)
    
    #Prints the sum of the rounded values:
    print(f"Rounded sum: {a1+b1+c1}")
    
round_sum()
