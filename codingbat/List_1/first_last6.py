'''
Given an array of ints, return True if 6 appears as either the first or last element in the array. 
The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False

'''
#Passing Positional Arguments: Checks the condition and returns the value.
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

#Runtime Variables:
def first_last6():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
    
    #Prints List: 
    print(array)

    #Checks the condition whether first or last element in the list is "6"
    if size >= 1:
        if array[0] == 6 or array[size-1] == 6:
            print("Hey! either of the ends contain '6' :)")
        else:
            print("Ohh! there's no '6' at the ends :(")
    else:
        print("Oops! list should contain atleast one element :(")

first_last6()
