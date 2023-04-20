def sum3():
    
    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)

    sum = 0
    for i in range(size):
        sum = sum + array[i]
    print(sum)

sum3()