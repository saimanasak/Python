'''
Code to execute a program where it takes runtime variables: array length, start variable, and interval range.
Sample Output:
        Enter size of array = 6
        Interval Range = 2
        Start from = 4

        Output array = [4, 6, 8, 8, 6, 4]

'''
def com_array():

    size = int(input("Enter size of the array: "))
    difference = int(input("Enter the difference: "))

    mid = int(size / 2)

    array = []

    value = int(input("Enter the starting element: "))

    array.append(value)

    for i in range(0, mid):

        f_value = array[i] + difference
        i += 1
        array.append(f_value)

    print(array)

    array1 = []

    for i in range(len(array)-2, -1, -1):

        array1.append(array[i])

    print(array1)

    print(array + array1)

com_array()
