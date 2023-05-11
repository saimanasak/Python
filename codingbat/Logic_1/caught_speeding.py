'''
You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. 
If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. 
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def caught_speeding(speed, is_birthday):
  if (speed <= 60 and is_birthday == False) or (speed <= 65 and is_birthday == True):
    return 0
  elif (((speed >= 61) and (speed <= 80)) and is_birthday == False) or (((speed >= 61) and (speed <= 85)) and is_birthday == True):
    return 1
  else:
    return 2

#Runtime Variables:
def caught_speeding():
    
    #Speed and birthday are declared and initialized:
    speed = int(input("Enter the speed: "))
    birthday = input("Is it birthday?(Yes|Y|y|No|N|n): ")
    
    #Conditions based on speed and birthday to check the rate of the ticket:
    if (speed <= 60 and birthday == "n") or (speed <= 65 and birthday == "y"):
        print("0")
    elif (((speed >= 61) and (speed <= 80)) and birthday == "n") or (((speed >= 61) and (speed <= 85)) and birthday == "y"):
        print("1")
    else:
        print("2")
        
caught_speeding()
