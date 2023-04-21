'''
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

'''
#Passing Positional Arguments: Returns the count of "hi" in the string
def count_hi(str):
  hi_count = str.count("hi")
  return hi_count

#Runtime Variables:
def count_hi():

    #String declaration and initialization:
    word = input("Enter a word which contains 'hi' : ")

    #Prints the count of "hi" in a string:
    print("No.of hi's : {}".format(word.count("hi")))

count_hi()
