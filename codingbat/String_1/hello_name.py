"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

"""

def hello_name():
    
    name = input("Enter name to greet: ")
    print("Hello {} !!!".format(name))

hello_name()