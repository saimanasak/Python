'''
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

'''
def middle_way():

    size1 = int(input("Enter size of the first array: "))
    array1 = []

    for i in range(size1):
        array1.append(int(input("Enter the value: ")))

    size2 = int(input("Enter size of the second array: "))
    array2 = []

    for i in range(size2):
        array2.append(int(input("Enter the value: ")))

    print(array1)
    print(array2)

    mid1 = int(size1 / 2)
    mid2 = int(size2 / 2)

    mid_array = [array1[mid1] , array2[mid2]]

    print("Mid array is : {}".format(mid_array))

middle_way()