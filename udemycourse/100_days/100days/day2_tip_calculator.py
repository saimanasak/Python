def tip_calculator():
    
    print("\nWelcome to Tip Calculator...\n")
    
    #Bill, Tip Percent, and Split Count initialization and declaration:
    bill = float(input("Enter the total bill(in $): "))
    tip_percent = int(input("Percentage of tip you would like to give (10, 12, or 15): "))
    split_count = int(input("No.of people to split the bill: "))
    
    #Calculates the tip amount:
    tip = (bill / 100) * tip_percent
    
    #Calculates the total bill:
    total_bill = bill + tip
    
    #Calculates the bill per person:
    person = total_bill / split_count
    
    #Prints the bill per person:
    print(f"\nEach person should pay: ${round(person, 2)}\n")
    
tip_calculator()
