'''
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 7 (every 6 will be followed by at least one 7). 
Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4

'''
#Passing Positional Arguments:
def sum67(nums):
  size = len(nums)
  temp1 = 0
  total = 0
  for i in range(size):
        if size == 0:
            return 0
        elif nums[i] == 6:
            temp1 = 6
        elif nums[i] == 7 and temp1 == 6:
            temp1 = 0
        elif nums[i] != 7 and temp1 == 6:
            total = total
        else:
            total = total + nums[i]
  return total

#Runtime Variables:
def sum67():
    
    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
    
    #Prints List:
    print(array)
    
    #Checks the conditions and prints the sum of the list:
    temp1 = 0
    total = 0
    for i in range(size):
        if size == 0:
            return 0
        elif array[i] == 6:
            temp1 = 6
        elif array[i] == 7 and temp1 == 6:
            temp1 = 0
        elif array[i] != 7 and temp1 == 6:
            total = total
        else:
            total = total + array[i]
    print("Sum : {}".format(total))
    
sum67()
