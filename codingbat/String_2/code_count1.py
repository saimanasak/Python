def code_count1():

    word = str(input("Enter the code word: "))
    count = 0
    for i in range(len(word)-3):
        if word[i] == "c" and word[i+1] == "o" and word[i+3] == "e":
            count += 1
            
    print("Count: {}".format(count))

code_count1()