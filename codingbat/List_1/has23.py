'''
Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False

'''
#Passing Positional Arguments: Checks for 2 and 3; and returns the value.
def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False

#Runtime Variables:
def has23():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []
    
    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
    
    #Prints List:
    print(array)

    #Condition to check whether the list has 2 or 3.  
    if 2 in array or 3 in array:
        print("Hey! the list contains 2/3 :)")
    else:
        print("Oops! there's no 2 or 3 in the list or the list is empty :(")

has23()
