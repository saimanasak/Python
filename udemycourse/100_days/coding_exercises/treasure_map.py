'''
******************* Problme Statement *********************

Write a program that will mark a spot with an X.
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what the nested list looks like:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']] 

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Mark a square on the map using a two-digit system. 
The first digit in the input will specify the column (the position on the horizontal axis).
The second digit in the input will specify the row number (the position on the vertical axis). 
So an input of 23 should place an X at the position

'''


#Rows, Map, and Position initialization and declaration:
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#Row and Column:
column = int(position[0])
row = int(position[1])

map[row-1][column-1] = 'X'

#Prints the final map:
print(f"{row1}\n{row2}\n{row3}")