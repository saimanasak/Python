'''
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.

'''
import time
def centered_average():
    
    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)
    
    max_value = max(array)
    min_value = min(array)
    total = 0
    
    start = time.time()
    for i in range(size):
        total = total + array[i]
    #i = 0
    #while i < size:
     #   total = total + array[i]
      #  i += 1
        
    end = time.time()
        
    average = int((total - max_value -min_value) / (size - 2))
    print("Average = {}".format(average))
    print(f"Start time : {start}")
    print(f"End time : {end}")
    print("Execution time : {} ms".format((end - start) * 10))
    
centered_average()
