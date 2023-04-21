'''
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

'''
#Passing Positional Arguments: Returns the middle elements of list (list length: 3)
def middle_way(a, b):
  return [a[1], b[1]]

#Runtime Variables:
def middle_way():

    #List Declaration: First List
    size1 = int(input("Enter size of the first list: "))
    array1 = []

    #List Initialization: First List
    for i in range(size1):
        array1.append(int(input("Enter the value: ")))

    #List Declaration: Second List
    size2 = int(input("Enter size of the second list: "))
    array2 = []

    #List Initialization: Second List
    for i in range(size2):
        array2.append(int(input("Enter the value: ")))

    #Prints both the lists:
    print(array1)
    print(array2)

    #Calculates the mid values for both the lists:
    mid1 = int(size1 / 2)
    mid2 = int(size2 / 2)
    mid_array = [array1[mid1] , array2[mid2]]
    
    #Prints the mid elements of both the lists:
    print("Mid element is : {}".format(mid_array))

middle_way()
