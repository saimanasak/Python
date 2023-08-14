#Import random module:
import random

#Colors:
Red = '\033[31m'
End = '\033[m'
Cyan = '\033[36m'
Yellow = '\033[33m'
Green = '\033[32m'
Blue = '\033[34m'
Pink = '\033[95m'

#Rock, Paper, and Scissors initialization and declaration:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)______
          ________)
          |_______
       ___________)
      (____)
---.__(___)
'''

gestures = [rock, paper, scissors]

#Generates a random gesture:
choose = random.randint(0, 2)

print(Cyan + "\nRock - 0, Paper - 1, Scissors - 2", End)
guess = int(input("\nChoose a number: "))

#Prints what computer chose randomly:
print(Pink + "\nYou Chose:", End)
print(Yellow + gestures[guess], End)

#Prints what an user chose:
print(Pink + "\nComputer Chose: ", End)
print(Yellow + gestures[choose], End)

#Conditions of game:
if guess == 0 and choose == 2:
    print(Green + "You Won\n", End)
elif guess == 1 and choose == 0:
    print(Green + "You Won\n", End)
elif guess == 2 and choose == 1:
    print(Green + "You Won\n", End) 
    
elif guess == 0 and choose == 1:
    print(Red + "You Lost\n", End)
elif guess == 1 and choose == 2:
    print(Red + "You Lost\n", End)
elif guess == 2 and choose == 0:
    print(Red + "You Lost\n", End)
    
else:
    print(Blue + "Tie.....!!!\n", End)
