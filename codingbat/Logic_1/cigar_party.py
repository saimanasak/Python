'''
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True

'''
#Passing Positional Arguments: Returns the value based on the conditions.
def cigar_party(cigars, is_weekend):
  if(cigars < 40)  or ((cigars > 60) and (is_weekend == False)):
    return False
  else:
    return True

#Runtime Variables:
def cigar_party():
    
    #Number of cigars intialization and declaration:
    cigar_count = int(input("Enter the number of cigars used: "))
    weekend = input("Is it weekend?(Yes|Y|y|No|N|n): ")
    
    #Checks the conditions of cigar count and the weekend and prints the success of a party:
    if(cigar_count < 40) or ((cigar_count > 60) and (weekend == "No") or (weekend == "N")):    
        print("Oops, it's not successful! Let's party again ;)")
    else:
        print("Hurray, it's successful party :)")      
          
cigar_party()
