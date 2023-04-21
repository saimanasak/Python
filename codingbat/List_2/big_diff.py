'''
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8

'''
#Passing Positional Arguments: Returns the difference of maximum and minimum values in the list.
def big_diff(nums):  
  return max(nums) - min(nums)

#Runtime Variables:
def big_diff():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)

    #Prints the difference of max and min elements of list:
    if size > 1:
        print("Difference of max and min elements: {}".format(max(array)-min(array)))
    else:
        print("Oops! list should contain atleast two elements :(")

big_diff()
