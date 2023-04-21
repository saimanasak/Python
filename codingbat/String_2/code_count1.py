'''
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2 

'''
#Passing Positional Arguments: Returns the count of "co?e" string
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i] == "c" and str[i+1] == "o" and str[i+3] == "e":
      count += 1
  return count

#Without importing:
#Runtime Variables: 
def code_count1():

    #String declaration and initialization:
    word = str(input("Enter the code word: "))
    
    #Checks for the regular expression "co?e":
    count = 0
    for i in range(len(word)-3):
        if word[i] == "c" and word[i+1] == "o" and word[i+3] == "e":
            count += 1
            
    #Prints the count:
    print("Count: {}".format(count))

code_count1()
