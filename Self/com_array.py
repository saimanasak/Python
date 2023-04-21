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

    if mid % 2 == 0:
        
        for i in range(len(array)-2, -1, -1):
            array1.append(array[i])
        print(array1)

        print(array + array1)

    array2 = []

    if mid % 2 != 0:
        
        for i in range(len(array)-1, -1, -1):
            array2.append(array[i])
    
        print(array2)

        print(array + array2)

com_array()
