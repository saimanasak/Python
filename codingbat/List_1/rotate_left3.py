def rotate_left3():

    array = []

    for i in range(0, 3):
        array.append(int(input("Enter the value: ")))

    temp = array[0]
    array[0] = array[1]
    array[1] = array[2]
    array[2] = temp

    print(array)

rotate_left3()