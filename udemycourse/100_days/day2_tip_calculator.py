def tip_calculator():
    
    print("\nWelcome to Tip Calculator...\n")
    
    bill = float(input("Enter the total bill(in $): "))
    tip_percent = int(input("Percentage of tip you would like to give (10, 12, or 15): "))
    split_count = int(input("No.of people to split the bill: "))
    
    tip = (bill / 100) * tip_percent
    
    total_bill = bill + tip
    
    person = total_bill / split_count
    
    print(f"\nEach person should pay: ${round(person, 2)}\n")
    
tip_calculator()
