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

#Letters, Symbols, and Numbers initialization and declaration:
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Prints welcome statement:
print(Pink + "\n****** Welcome to PASSWORD generator ******", End)

#Count of letters, numbers, and symbols are initialized and declared:
letters_count = int(input("\nNumber of letters you would like to have?\n"))
symbols_count = int(input("\nNumber of symbols you would like to have?\n"))
numbers_count = int(input("\nNumber of numbers you would like to have?\n"))

#Lists to store the randomly chosen letters, symbols, and numbers:
letter_list = []
symbol_list = []
number_list = []

#Loops to choose the randomly chosen characters and store them in a list:
for lc in range(letters_count):
    random_letter = random.choice(letters)
    letter_list.append(random_letter)
    
for sc in range(symbols_count):
    random_symbol = random.choice(symbols)
    symbol_list.append(random_symbol)

for nc in range(numbers_count):
    random_number = random.choice(numbers)
    number_list.append(random_number)
    
#print(letter_list)
#print(symbol_list)
#print(number_list)

#Concatenates the 3 lists:
combine = letter_list + symbol_list + number_list
#print(combine)

#Method to shuffle the list:
random.shuffle(combine)

#join method converts the list into a string:
password = ''.join(combine)

#Prints the final generated password:
print(Green + "\nYour password is: {}\n".format(password), End)

print(Cyan + "Keep it secure.... ;) \n", End)