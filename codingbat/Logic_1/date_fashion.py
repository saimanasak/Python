'''
You and your date are trying to get a table at a restaurant. 
The parameter "you" is the stylishness of your clothes, in the range 0..10, and 
"date" is the stylishness of your date's clothes. 
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
If either of you is very stylish, 8 or more, then the result is 2 (yes). 
With the exception that if either of you has style of 2 or less, then the result is 0 (no). 
Otherwise the result is 1 (maybe).

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def date_fashion(you, date):
  if (you >= 8 and date > 2) or (date >= 8 and you > 2):
    return 2
  elif (you <= 2) or (date <= 2):
    return 0
  else:
   return 1

#Runtime Variables:
def date_fashion():

    #Rating of stylishness initialization and declaration: 
    yours = int(input("Rate the stylishness of your outfit (out of 10): "))
    your_date = int(input("Rate the stylishness of your partner's outfit (out of 10): "))

    #Checks the conditions based on yours and your partner's stylishness and assigns a table:
    if (yours >= 8 and your_date > 2) or (your_date >= 8 and yours > 2):
        print("2")
    elif (yours <= 2) or (your_date <= 2):
        print("0")
    else:
        print("1")

date_fashion()
