'''
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come 
immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''
#Passing Positional Arguments: Checks the conditions and returns the sum.
def sum13(nums):
  size = len(nums)
  total = 0
  for i in range(size):
    if size ==0:
      return 0
    elif nums[i] == 13 or nums[i-1] == 13 and i > 0:
      i = i + 1
    else:
      total = total + nums[i]
  return total

#Runtime Variables:
def sum13():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    stop = int(input("Enter the value to stop: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: "))) 
    
    #Prints List:
    print(array)
    
    #Checks for the stop value and prints the sum of list:
    total = 0
    for i in range(size):
        if size == 0:
            return 0
        elif array[i] == stop or array[i-1] == stop and i > 0:
            i += 1
        else:
            total = total + array[i]
    print("Sum: {}".format(total))

sum13()
