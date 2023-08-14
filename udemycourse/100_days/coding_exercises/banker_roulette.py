'''
Write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names.
For this to work, you must enter all the names as names followed by comma then space. 
e.g. name, name, name

'''

#Import random module:
import random

#List Declaration:
size = int(input("Enter size of the list: "))
array = []

#List Initialization:
for i in range(size):
    array.append(input("Enter names: "))

#Picks a person randomly:
lucky = random.randint(0, size-1)

#Prints who is going to buy the meal:
print("{} is going to buy the meal today!".format(array[lucky]))


#Another way:
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

size = len(names)
lucky = random.randint(1, size)

print("{} is going to buy the meal today!".format(names[lucky]))
