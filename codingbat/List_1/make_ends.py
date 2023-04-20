'''
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. 
The original array will be length 1 or more.

'''
def make_ends():

    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)

    if size > 1:
        ends_array = [array[0], array[size-1]]
        print("End values are: {}".format(ends_array))
    elif size == 1:
        print("End values are: {}".format(array[0]))
    else:
        print("List should contain atleast one element :(")      
        
make_ends()