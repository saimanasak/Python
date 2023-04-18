'''
To calculate (a+b)^n

'''
from sympy import init_printing, Symbol, expand
init_printing()
def power():

    a = Symbol("a")
    b = Symbol("b")
    power = int(input("Enter the expo value: "))
    formula = (a + b)**power
    
    print("Formula = {}".format(formula.expand()))

power()