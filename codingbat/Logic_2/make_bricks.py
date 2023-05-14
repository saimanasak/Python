'''
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def make_bricks(small, big, goal):
  s = small * 1
  b = big * 5
  total = s + b
    
  if goal > total:
    return False
  elif goal % 5 > small:
    return False
  else:
    return True

#Runtime Variables:
def make_bricks():
    
    #No.of small, big and the goal are initialized and declared:
    small = int(input("Enter no.of small (1-inch) bricks: "))
    big = int(input("Enter no.of big (5-inch) bricks: "))
    goal = int(input("Enter the goal of bricks: "))
    
    #Final values of the bricks:
    s = small * 1
    b = big * 5
    
    #Checks the conditions based on the goal and prints:
    if goal >= b:
        value = goal - b
    else:
        value = goal % 5
    if s >= value:
        print("Goal can be achieved :)")
    else:
        print("Goal can't be reached :(")
    
make_bricks()
