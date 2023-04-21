'''
Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
'''
#Passing Positional Arguments:
def max_end3(nums):
  if nums[0] > nums[2]:
    return [nums[0], nums[0], nums[0]]
  else:
    return [nums[2], nums[2], nums[2]]

#Runtime Variables:
def max_end():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)

    #Checks the first element of list if it is larger value.
    if array[0] > array[size-1]:
        for i in range(size):
            array[i] = array[0]

    #Checks the last element of list if it is larger value.
    if array[0] < array[size-1]:
        for i in range(size):
            array[i] = array[size-1]

    #Prints the list with largest value.
    print("Max array: {}".format(array))

max_end()
