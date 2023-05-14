'''
We have a loud talking parrot.
The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  else:
    return False

#Runtime Variables:
def parrot_trouble():
    
    #Talking and time status: Initialization and declaration:
    talking = input("Is parrot talking??? (y or n) ")
    time = int(input("Enter the time at which parrot is talking: "))
    
    #Checks the conditions and returns the status of situations:
    if talking == "y" and (time < 7 or time > 20):
        print("Oh no! We are in trouble :( ")
    else:
        print("Hurray! We aren't in trouble :) ")

parrot_trouble()
 