'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False

'''
#Passing Positional Arguments: Checks the conditions and returns the count.                                                                          
def has22(nums):
  size = len(nums)
  for i in range(1, size):
    if size>1 and nums[i] == 2 and nums[i-1] == 2:
      return True
  return False

#Runtime Variables:
def has22():
    
    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)
    
    #Checks if there are consecutive 2's in the list and then prints the count:
    c = 0
    for i in range(1,size):
        if size>1 and array[i] == 2 and array[i-1] == 2:
            c += 1
    if c > 0:
        print("Count: {}".format(c))
    else:
        print("Oops, there are no consecutive 2's or list is empty :(")     
has22()
