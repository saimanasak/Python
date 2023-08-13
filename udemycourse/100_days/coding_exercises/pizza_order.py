'''
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1

'''

Pink = '\033[95m'
End = '\033[m'

print(Pink + "\nWelcome to Python Pizza Deliveries!!!", End)

size = input("\nWhat size pizza do you want? (S, M, or L) - ")
add_pepperoni = input("Do you want pepperoni? (Y or N) -  ")
extra_cheese = input("Do you want extra cheese? (Y or N) - ")

small = 15
medium = 20
large = 25
pep_s = 2
pep_m_l = 3
cheese = 1 
bill = 0 

if size == 'S':
    if add_pepperoni == "Y":
        bill = bill + small + pep_s
    elif add_pepperoni == "N":
        bill = bill + small
            
if size == 'M':
    if add_pepperoni == "Y":
        bill = bill + medium + pep_m_l
    elif add_pepperoni == "N":
        bill = bill + medium

if size == 'L':
    if add_pepperoni == "Y":
        bill = bill + large + pep_m_l
    elif add_pepperoni == "N":
        bill = bill + large

if extra_cheese == "Y":
    print("\nYour final bill is: ${}.".format(bill+cheese))
else:
    print("\nYour final bill is: ${}.".format(bill))
