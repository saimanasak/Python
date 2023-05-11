'''
The squirrels in Palo Alto spend most of the day playing. 
In particular, they play if the temperature is between 60 and 90 (inclusive). 
Unless it is summer, then the upper limit is 100 instead of 90. 
Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def squirrel_play(temp, is_summer):
  if ((temp >= 60) and (temp <= 90)) and ((is_summer == False)):
    return True
  elif ((temp >= 60) and (temp <= 100)) and ((is_summer == True)):
    return True
  else:
    return False

#Runtime Variables:
def squirrel_play():
    
    #Temperature and is it summer or not intialization and declaration:
    temp = int(input("Enter the temperature: "))
    summer = input("Is it summer?(Yes|Y|y|No|N|n): ")
    
    #Conditions based on temperatures to check whether squirrels should play or not: 
    if ((temp >= 60) and (temp <= 90)) and ((summer == "No") or (summer == "N") or (summer == "n")):
        print("Hurray! Let's play :) ")
    elif ((temp >= 60) and (temp <= 100)) and ((summer == "Yes") or (summer == "Y")or (summer == "y")):
        print("Hurray! Let's play :) ")
    else:
        print("Oh no! Don't play :( ")

squirrel_play()
