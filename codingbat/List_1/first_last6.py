'''
Given an array of ints, return True if 6 appears as either the first or last element in the array. 
The array will be length 1 or more.

'''
def first_last6():

    size = int(input("Enter size of the array: "))

    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))

    print(array)

    if size >= 1:
        if array[0] == 6 or array[size-1] == 6:
            print("True!!!")
        else:
            print("False!!!")
    else:
        print("List should contain atleast one element")

first_last6()
