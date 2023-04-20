'''
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

'''
def reverse3():

    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)

    array.reverse()
    print("Reversed array : {}".format(array))

reverse3()