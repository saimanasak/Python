def count_evens():

    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)

    count = 0
    for i in range(size):
        if array[i] % 2 == 0:
            count += 1
    print(count)

count_evens()