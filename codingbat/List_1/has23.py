'''
Given an int array length 2, return True if it contains a 2 or a 3.

'''
def has23():

    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)

    if 2 in array or 3 in array:
        print("Hey, the list contains 2/3 :)")
    else:
        print("There's no 2 or 3 in the list or the list is empty :(")

has23()