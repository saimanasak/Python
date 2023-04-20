'''

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

'''
def same_first_last():

    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)
    
    if size >= 1:
        if array[0] == array[size-1]:
            print("True!!!")
        else:
            print("False!!!")
    else:
        print("List should contain atleast one element!!!")

same_first_last()