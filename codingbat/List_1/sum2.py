'''
Given an array of ints, return the sum of the first 2 elements in the array. 
If the array length is less than 2, just sum up the elements that exist, 
returning 0 if the array is length 0.

'''
def sum2():

    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)

    if size > 1:   
        sum = array[0] + array[1]
        print(sum)
    elif size == 1:
        print(array[0])
    else:
        print("List should contain atleast one element :(")

sum2()