'''
*********************** Problem Statement ************************

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left 
if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

'''
#Age initialization and declaration:
age = input("What is your current age? ")
a = int(age)

#No.of years left:
left = 90 - a

#Calculates no.of days, weeks, and months:
days = left * 365
weeks = left * 52
months = left * 12

#Prints the no.of days, months, weeks left:
print("You have {} days, {} weeks, and {} months left.".format(days, weeks, months))
