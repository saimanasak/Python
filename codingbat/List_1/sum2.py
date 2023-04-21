'''
Given an array of ints, return the sum of the first 2 elements in the array. 
If the array length is less than 2, just sum up the elements that exist, 
returning 0 if the array is length 0.

sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2

'''
#Passing Positional Arguments: Adding first elements of the list and returns the final value.
def sum2(nums):
  length = len(nums)
  if length > 1:
    return nums[0] + nums[1]
  if length == 0:
    return 0
  if length == 1:
    return nums[0]

#Runtime Variables
def sum2():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)

    #Checks the conditions and prints the result.
    if size > 1:   
        sum = array[0] + array[1]
        print("Sum of first 2 elements: {}".format(sum))
    elif size == 1:
        print("Sum: {}".format(array[0]))
    else:
        print("List should contain atleast one element :(")

sum2()
