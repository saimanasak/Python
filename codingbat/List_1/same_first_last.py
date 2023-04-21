'''
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True

'''
#Passing Positional Arguments: Checks if both the end elements are same and returns the values.
def same_first_last(nums):
  length = len(nums)
  if length >= 1:
    if nums[0] == nums[length-1]:
      return True
    else:
      return False
  else:
    return False

#Runtime Variables:
def same_first_last():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)
    
    #Condition to compare both the end elements of list:
    if size >= 1:
        if array[0] == array[size-1]:
            print("Hey! both the end values are same :)")
        else:
            print("Ohh, end values aren't same :(")
    else:
        print("Oops! list should contain atleast one element :(")

same_first_last()
