'''
******************** Problem Statement ***********************

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of someone's weight taking into account their height. e.g. 
If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI = weight (kg) / height^2 (m^2)

'''
#Height and Weight initialization and declaration:
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#Conversion:
w = int(weight)
h = float(height)

#Formula to calculate BMI:
bmi = w / (h * h)

#Prints the calculated BMI value:
print(round(bmi))