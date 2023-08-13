'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

'''

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/(height*height)

if bmi < 18.5:
    print("Your BMI is {}, you are underweight.".format(round(bmi)))
elif bmi > 18.5 and bmi < 25:
    print("Your BMI is {}, you have a normal weight.".format(round(bmi)))
elif bmi > 25 and bmi < 30:
    print("Your BMI is {}, you are slightly overweight.".format(round(bmi)))
elif bmi > 30 and bmi < 35:
    print("Your BMI is {}, you are obese.".format(round(bmi)))
else:
    print("Your BMI is {}, you are clinically obese.".format(round(bmi)))