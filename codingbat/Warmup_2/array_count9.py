'''
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def array_count9(nums):
  c=0
  for i in nums:
    if i == 9:
      c += 1
  return c

#Runtime Variables:
def array_count9():
    
    #List Declaration:
    #Size and Count initialization and declaration:
    size = int(input("Enter size of the list: "))
    count = 0
    array = []
    
    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
    
    #Checks for the value "9" in array and increases the count:
    for i in array:
        if i == 9:
            count = count + 1
    
    #Prints the final count of 9s:
    print(f"No.of 9's: {count}")
    
array_count9()
