'''
Given 2 arrays of ints, a and b, return True if they have the same first element 
or they have the same last element. 
Both arrays will be length 1 or more.

'''
'''
def common_end(a, b):
  
  if (len(a)) >=1 and (len(b)) >=1:
    if (a[len(a)-1] == b[len(b)-1]) or (a[0] == b[0]):
      return True
    else:
      return False
  else:
    return False

'''
def common_end():

    #First List:
    size1 = int(input("Enter size of the first array: "))
    array1 = []
    for i in range(size1):
        array1.append(int(input("Enter the value: ")))

    #Second List:
    size2 = int(input("Enter size of the second array: "))
    array2 = []
    for i in range(size2):
        array2.append(int(input("Enter the value: ")))
        
    #Printing two given arrays:
    print(array1)
    print(array2)
    
    #Conditions to check if both the common ends are same or not:
    if size1 >=1 and size2 >=1:
        if (array1[size1-1] == array2[size2-1]) or (array1[0] == array2[0]):
            print("True!!!")
        else:
            print("False!!!")
    else:
        print("Array should contain atleast one element!!!")

common_end()
