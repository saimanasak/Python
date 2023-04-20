'''
Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
and set all the other elements to be that value. Return the changed array.

'''
def max_end():

    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)

    if array[0] > array[size-1]:
        for i in range(size):
            array[i] = array[0]

    if array[0] < array[size-1]:
        for i in range(size):
            array[i] = array[size-1]

    print("Max array: {}".format(array))

max_end()
