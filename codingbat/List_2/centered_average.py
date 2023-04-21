'''
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3

'''
#Passing Positional Arguments: Calculates the mean average and returns it.
def centered_average(nums):  
  size = len(nums)
  max_value = max(nums)
  min_value = min(nums)
  total = 0
  for i in range(size):
    total = total + nums[i]
  average = int((total - max_value - min_value) / (size - 2))
  return average

#Runtime Variables:
import time
def centered_average():
    
    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)
    
    #Finding the maximum and minimum values from the list:
    max_value = max(array)
    min_value = min(array)
    total = 0
    
    #Starting execution time before starting the "for" loop:  
    start = time.time()
    
    #Loop to calculate the sum of all the elements in the list:
    for i in range(size):
        total = total + array[i]
    '''
    "while" loop:
    i = 0
    while i < size:
       total = total + array[i]
      i += 1
    '''
    
    #Final execution time after completing the "for" loop:
    end = time.time()
    
    #Calculate the mean average of the list and prints the value:
    average = int((total - max_value -min_value) / (size - 2))
    print("Average = {}".format(average))
    
    #Prints the execution time of "for" loop before and after:
    print(f"Start time : {start}")
    print(f"End time : {end}")
    
    #Total execution time:
    print("Execution time : {} ms".format((end - start) * 10**3))
    
centered_average()
