Pink = '\033[95m'
End = '\033[m'
Cyan = '\033[36m'
Green = '\033[32m'

def band_name_generator():
    
    print(Pink + "\nWelcome to the Band Name Generator...\n", End)
    
    city = input("Enter your city: ")
    pet = input("Enter your pet name: ")

    print(Cyan + "\nYour band name could be:", End + Green + f"{city + ' ' + pet}\n", End)
    
band_name_generator()
