'''
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. 
The original array will be length 1 or more.

make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]

'''
#Passing Positional Arguments: Returns the end values of a list.
def make_ends(nums):
  length = len(nums)
  return [nums[0], nums[length-1]]

#Runtime Variables:
def make_ends():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)

    #Prints the elements based on the conditions satisfied:
    if size > 1:
        ends_array = [array[0], array[size-1]]
        print("End values are: {}".format(ends_array))
    elif size == 1:
        print("End values are: {}".format(array[0]))
    else:
        print("List should contain atleast one element :(")      
        
make_ends()
