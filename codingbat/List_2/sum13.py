'''
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come 
immediately after a 13 also do not count.

'''
def sum13():

    size = int(input("Enter size of the array: "))
    stop = int(input("Enter the value to stop: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: "))) 
    print(array)
    
    total = 0
    for i in range(size):
        if size == 0:
            return 0
        elif array[i] == stop or array[i-1] == stop and i > 0:
            i += 1
        else:
            total = total + array[i]
    print(total)

sum13()
