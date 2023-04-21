'''
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0

'''
#Passing Positional Arguments: Counts the number of even numbers and returns the final count.
def count_evens(nums):  
  c = 0 
  for i in nums:
    if i % 2 == 0:
      c += 1
  return c

#Runtime Variables:
def count_evens():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)

    #Checks for the even values and prints the final count:
    count = 0
    for i in range(size):
        if array[i] % 2 == 0:
            count += 1
    print("Total number of even values: {}".format(count))

count_evens()
