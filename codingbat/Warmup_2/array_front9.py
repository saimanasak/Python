'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def array_front9(nums):
  c = 0
  length = min(len(nums), 4)
  
  for i in range(length):
    if nums[i] == 9:
      c += 1
  
  if c > 0:
    return True
  else:
    return False

#Runtime Variables:
def array_front9():
    
    #List Declaration:
    #Size and Count initialization and declaration:
    size = int(input("Enter size of the list: "))
    array = []
    count = 0
    
    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
    
    #Assigns the minimum array size to first_ele:
    first_ele = min(size, 4)
    
    #Loop to check the first 4 elements for "9":
    for i in range(first_ele):
        if array[i] == 9:
            count = count + 1
    
    #Prints the result based on the final count value:
    if count > 0:
        print("There's 9 in the list.")
    else:
        print("There's no 9 in the list.")
            
array_front9()
