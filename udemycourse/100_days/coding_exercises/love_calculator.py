'''
******************* Problem Statement ******************

Write a program that tests the compatibility between two people.

To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **, you are alright together."

Otherwise, the message will just be their score.
"Your score is **."

'''

Pink = '\033[95m'
End = '\033[m'

print(Pink + "\nWelcome to the Love Calculator!!!", End)
name1 = input("\nWhat is your name? \n")
name2 = input("What is your partner name? \n")

true = love = 0

for n1 in name1.upper():
    if n1 == "T" or n1 == "R" or n1 == "U" or n1 == "E":
        true = true + 1
    if n1 == "L" or n1 == "O" or n1 == "V" or n1 == "E":
        love = love + 1

for n2 in name2.upper():
    if n2 == "T" or n2 == "R" or n2 == "U" or n2 == "E":
        true = true + 1
    if n2 == "L" or n2 == "O" or n2 == "V" or n2 == "E":
        love = love + 1

love_score = true*10+love

if love_score < 10 or love_score > 90:
    print("\nYour score is {}, you go together like coke and mentos.\n".format(love_score))
elif love_score > 40 and love_score < 50:
    print("\nYour score is {}, you are alright together.\n".format(love_score))
else:
    print("\nYour score is {}.\n".format(love_score))