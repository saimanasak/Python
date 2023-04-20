'''
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 7 (every 6 will be followed by at least one 7). 
Return 0 for no numbers.

'''
def sum67():
    
    size = int(input("Enter size of the array: "))
    array = []

    for i in range(size):
        array.append(int(input("Enter the value: ")))
    print(array)
    
    temp1 = 0
    total = 0
    for i in range(size):
        if size == 0:
            return 0
        elif array[i] == 6:
            temp1 = 6
        elif array[i] == 7 and temp1 == 6:
            temp1 = 0
        elif array[i] != 7 and temp1 == 6:
            total = total
        else:
            total = total + array[i]
    print(total)
    
sum67()
