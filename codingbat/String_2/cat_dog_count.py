'''
Return True if the string "cat" and "dog" appear same number of times in the given string.

'''

def cat_dog_count():

    word = input("Enter a word: ")

    if word.count("cat") == word.count("dog"):
        print("True!!!")
    else:
        print("False!!!")

cat_dog_count()