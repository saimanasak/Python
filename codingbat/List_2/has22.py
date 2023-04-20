'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

'''
def has22():
    
    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)
    
    c = 0
    for i in range(1,size):
        if size>1 and array[i] == 2 and array[i-1] == 2:
            c += 1
            print(i)
    if c > 0:
        print(True)
        print(c)
    else:
        print(False)     
has22()
