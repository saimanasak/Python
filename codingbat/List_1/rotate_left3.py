'''
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]

'''
#Passing Positional Arguments: Returns the rotated left element list.
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

#Runtime Variables:
def rotate_left3():

    ##List Declaration: List should be of length 3 elements only.
    array = []

    #List Initialization:
    for i in range(0, 3):
        array.append(int(input("Enter the value: ")))

    #Rotate Left:
    temp = array[0]
    array[0] = array[1]
    array[1] = array[2]
    array[2] = temp

    #Prints List:
    print(array)

rotate_left3()
