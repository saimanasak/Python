'''
Given an array of ints, return True if the sequence of 
numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

'''

#Passing Positional Arguments: Returns the value based on the conditions.
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

#Runtime Variables:
def array123():
    
    #List Declaration:
    #Size and Count initialization and declaration:
    size = int(input("Enter size of the list: "))
    array = []
    count = 0
    
     #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
    
    #Checks for the sequence:
    for i in range(size):
        if array[i] == 1 and array[i + 1] == 2 and array[i + 2] == 3:
            count = count + 1

    #Prints the result based on the sequence:
    if count > 0:
        print("There's a 123 sequence in the list.")
    else:
        print("There's no 123 sequence in the list.")
        
array123()
