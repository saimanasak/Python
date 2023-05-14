'''
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def make_chocolate(small, big, goal):
  
  s = small * 1
  b = big * 5
  
  if goal >= b:
    value = goal - b
  else:
    value = goal % 5
        
  if value <= small:
    return value
  else:
    return -1

#Runtime Variables:
def make_chocolate():
    
    #3 numbers' initialization and declaration:
    small = int(input("Enter no.of small (1-kilo) bars: "))
    big = int(input("Enter no.of big (5-kilos) bars: "))
    goal = int(input("Enter the goal of bars: "))
    
    #Values from bar values:
    s = small * 1
    b = big * 5
    
    #Checks the conditions based on the goal bars and prints the used small bars:
    if goal >= b:
        value = goal - b
    else:
        value = goal % 5
        
    if value <= small:
        print(f"Used small chocolate bars: {value}")
    else:
        print("Goal can't be reached!!")
        
make_chocolate()
