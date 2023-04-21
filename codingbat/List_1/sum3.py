'''
Given an array of ints length 3, return the sum of all the elements.

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
'''
#Passing Positional Arguments: Returns the sum of all the elements in the list.
def sum3(nums):
  size = len(nums)
  sum = 0  
  for i in range(size):
    sum = sum + nums[i]  
  return sum

#Runtime Variables:
def sum3():
    
    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)

    #Adds all the elements of the list and prints.
    sum = 0
    for i in range(size):
        sum = sum + array[i]
    print("Sum of all the elements: {}".format(sum))

sum3()
