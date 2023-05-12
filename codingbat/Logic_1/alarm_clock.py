'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, 
and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. 
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def alarm_clock(day, vacation):
  if vacation == True:
    if day >= 1 and day <= 5:
      return "10:00"
    else:
      return "off"
  else:
    if day >= 1 and day <= 5:
      return "7:00"
    else:
      return "10:00"

#Runtime Variables:
def alarm_clock():
    
    #Day and Vacation declaration and initialization:
    num = int(input("Enter a day (0 to 6) - "))
    vacation = input("Are you on vacation??? (y or n) ")
    
    #Checks the conditions based on the week and vacation and rings the alarm:
    if vacation == "y":
        if num >= 1 and num <= 5:
            print("10:00")
        else:
            print("off")
    else:
        if num >= 1 and num <= 5:
            print("7:00")
        else:
            print("10:00")
            
alarm_clock()
