'''
The parameter weekday is True if it is a weekday, 
and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. 
Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False

#Runtime Variables:
def sleep_in():
    
    #Vacation and Weekday initialization and declaration:
    weekday = input("Is it weekday??? (y or n) ")
    vacation = input("Are you on vacation??? (y or n) ")
    
    #Checks the condition and prints the update about sleep:
    if weekday == "n" or vacation == "y":
        print("Hurray! We can sleep :) ")
    else:
        print("Oh no! We can't sleep :(")

sleep_in()
