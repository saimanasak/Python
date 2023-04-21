'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

'''
#Passing Positional Arguments: Returns the greetings
def hello_name(name):
  return "Hello " + name + "!"

#Runtime Variables:
def hello_name():
    
    #String declaration and initialization:
    name = input("Enter name to greet: ")
    
    #Greetings:
    print("Hello {} !!!".format(name))

hello_name()
