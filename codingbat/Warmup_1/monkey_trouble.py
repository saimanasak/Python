'''
We have two monkeys, a and b, and the parameters a_smile and b_smile
indicate if each is smiling. 
We are in trouble if they are both smiling or if neither of them is smiling.
Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile == True or a_smile == b_smile == False:
    return True
  else:
    return False

#Runtime Variables:
def monkey_trouble():
    
    #Status of monkey's smiling: initialization and declaration:
    monkey1 = input("Is first monkey smiling??? (y or n) ")
    monkey2 = input("Is second monkey smiling??? (y or n) ")
    
    #Checks the conditions and prints the situations:
    if monkey1 == monkey2 == "y" or monkey1 == monkey2 == "n":
        print("Oh no! We are in trouble :( ")
    else:
        print("Hurray! We aren't in trouble :) ")
        
monkey_trouble()
