'''
Given 2 arrays of ints, a and b, return True if they have the same first element 
or they have the same last element. 
Both arrays will be length 1 or more.

'''
def common_end():

    size1 = int(input("Enter size of the first array: "))

    array1 = []

    for value1 in range(size1):

        value1 = input("Enter the value for the first array: ")
        val_int1 = int(value1)
        array1.append(val_int1)

    size2 = int(input("Enter size of the second array: "))

    array2 = []

    for value2 in range(size2):

        value2 = input("Enter the value for the second array: ")
        val_int2 = int(value2)
        array2.append(val_int2)

    print(array1)
    print(array2)

    if size1 >=1 and size2 >=1:
        if (array1[size1-1] == array2[size2-1]) or (array1[0] == array2[0]):
            print("True!!!")
        else:
            print("False!!!")
    else:
        print("Array should contain atleast one element!!!")

common_end()
