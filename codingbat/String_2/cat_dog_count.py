'''
Return True if the string "cat" and "dog" appear same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

'''
#Passing Positional Arguments: Returns either True or False based on the count
def cat_dog(str):
  if str.count("cat") == str.count("dog"):
    return True
  else:
    return False

#Runtime Variables:
def cat_dog_count():

    #String declaration and initialization:
    word = input("Enter a word: ")

    #Checks if both the "dog" and "cat" count is same and prints:
    if word.count("cat") == word.count("dog"):
        print("Same count!!!")
    else:
        print("Oops, it's not same!!!")

cat_dog_count()
