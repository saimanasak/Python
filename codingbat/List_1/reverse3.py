'''
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]

'''
#Passing Positional Arguments: Returns the reversed element list.
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

#Runtime Variables:
def reverse3():

    #List Declaration:
    size = int(input("Enter size of the list: "))
    array = []

    #List Initialization:
    for i in range(size):
        array.append(int(input("Enter the value: ")))
        
    #Prints List:
    print(array)

    #List is reversed and prints the reversed list:
    array.reverse()
    print("Reversed list : {}".format(array))

reverse3()
