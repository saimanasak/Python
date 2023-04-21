'''
Given 2 arrays of ints, a and b, return True if they have the same first element 
or they have the same last element. 
Both arrays will be length 1 or more.

common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

'''
#Passing Positional Arguments: Checks the condition and returns the value.
def common_end(a, b):  
  if (len(a)) >=1 and (len(b)) >=1:
    if (a[len(a)-1] == b[len(b)-1]) or (a[0] == b[0]):
      return True
    else:
      return False
  else:
    return False

#Runtime Variables:
def common_end():

    #First List:
    size1 = int(input("Enter size of the first list: "))
    array1 = []
    for i in range(size1):
        array1.append(int(input("Enter the value: ")))

    #Second List:
    size2 = int(input("Enter size of the second list: "))
    array2 = []
    for i in range(size2):
        array2.append(int(input("Enter the value: ")))
        
    #Printing two given lists:
    print(array1)
    print(array2)
    
    #Conditions to check if both the common ends are same or not:
    if size1 >= 1 and size2 >= 1:
        if (array1[size1-1] == array2[size2-1]) or (array1[0] == array2[0]):
            print("Hey! both the lists have the common end :)")
        else:
            print("Ohh! there's no common end :(")
    else:
        print("Oops! list should contain atleast one element :(")

common_end()
