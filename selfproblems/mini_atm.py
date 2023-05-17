'''
MINI ATM - Here, a person can create a bank account, deposit, 
withdraw, check personal information, check balance, and can close the account.
Authenticates the user's info.
Used SQL database to store the user's information.

'''

#Imported modules to system and to connect to MYSQL:
import sys
import mysql.connector

#Colors initialization and declaration:
#Used ANSI escape codes:
Red = '\033[31m'
End = '\033[m'
Cyan = '\033[36m'
Yellow = '\033[33m'
Green = '\033[32m'
Blue = '\033[34m'
Pink = '\033[95m'

#Connection setup with mysql:
myconnection = mysql.connector.connect(host = "localhost", user = "root",passwd = "MySQL@1212", database = "customers")

#Cursor is created w.r.t. mysql connection:
cursor = myconnection.cursor()

#DATABASE CREATION:
#cursor.execute("CREATE DATABASE customers")
#print("Created Successfully")

#TABLE CREATION:
#cursor.execute("CREATE TABLE customer_info(NAME varchar(255), AGE int,GENDER varchar(30), GOVT_ID int, MOBILE_NUMBER int, BALANCE int);")
#print("Table created Successfully")

def mini_atm():
    
    #Function for account creation:
    def create_account():
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        govt_id = int(input("Enter government issued id number: "))
        mobile = int(input("Enter mobile number: "))
        deposit = int(input("Enter the amount to be deposited: "))
        
        #SQL Query to insert the created info into the table:
        my_sql = "INSERT INTO customer_info (NAME, AGE, GENDER, GOVT_ID, MOBILE_NUMBER, BALANCE) VALUES (%s, %s, %s, %s, %s, %s);"
        values = (name, age, gender, govt_id, mobile, deposit)
        
        cursor.execute(my_sql, values)
        
        myconnection.commit()
        
        print(Green + "Your account has been created successfully :) ", End)
    
    #Function to deposit:  
    def deposit():
        name_1 = input("Enter your name: ")
        govt_id_1 = int(input("Enter government issued id number: "))
        
        my_sql = "SELECT NAME, GOVT_ID, BALANCE FROM customer_info"
        cursor.execute(my_sql)
        information = cursor.fetchall()
        
        for column in information:
            name_check = column[0]
            id_check = column[1]
            bal = column[2]
            
            if name_1 == name_check and govt_id_1 == id_check:
                d = int(input("Enter the amount to be deposited: "))
                
                amount = d + bal
                
                my_sql1 = "UPDATE customer_info SET BALANCE = %s WHERE GOVT_ID = %s"
                values = (amount, govt_id_1)
                
                cursor.execute(my_sql1, values)
                myconnection.commit()
                
                print(Green + "Deposit successful", End)
                print(f"Available Balance: {amount}")
                print('\n')
                break
        else:
            print(Red + "User not found", End)
            print('\n')
       
    #Function to withdraw money: 
    def withdraw():
        name_1 = input("Enter your name: ")
        govt_id_1 = int(input("Enter government issued id number: "))
        
        my_sql = "SELECT NAME, GOVT_ID, BALANCE FROM customer_info"
        cursor.execute(my_sql)
        information = cursor.fetchall()
        
        for column in information:
            name_check = column[0]
            id_check = column[1]
            bal = column[2]
            
            if name_1 == name_check and govt_id_1 == id_check:
                w = int(input("Enter the amount to withdraw: "))
                
                amount = bal - w
                
                my_sql1 = "UPDATE customer_info SET BALANCE = %s WHERE GOVT_ID = %s"
                values = (amount, govt_id_1)
                
                cursor.execute(my_sql1, values)
                myconnection.commit()
                
                print(Green + "Withdraw is done.", End)
                print(f"Available Balance: {amount}")
                print('\n')
                break
        else:
            print(Red + "User not found", End)
            print('\n')
    
    #Function to check the balance:   
    def check_balance():
        name_1 = input("Enter your name: ")
        govt_id_1 = int(input("Enter government issued id number: "))
        
        my_sql = "SELECT NAME, GOVT_ID, BALANCE FROM customer_info"
        cursor.execute(my_sql)
        information = cursor.fetchall()
        
        for column in information:
            name_check = column[0]
            id_check = column[1]
            bal = column[2]
            
            if name_1 == name_check and govt_id_1 == id_check:
                print(f"Available Balance: {bal}")
                print('\n')
                break
        else:
            print(Red + "User not found", End)
            print('\n')
    
    #Function to close the account:  
    def close_account():
        name_1 = input("Enter your name: ")
        govt_id_1 = int(input("Enter government issued id number: "))
        
        my_sql = "SELECT NAME, GOVT_ID, BALANCE FROM customer_info"
        cursor.execute(my_sql)
        information = cursor.fetchall()
        
        for column in information:
            name_check = column[0]
            id_check = column[1]
            bal = column[2]
            
            if name_1 == name_check and govt_id_1 == id_check:
                my_sql1 = "DELETE FROM customer_info WHERE GOVT_ID = %s"
                values = (govt_id_1)
                
                cursor.execute(my_sql1, values)
                myconnection.commit()
                
                print(Cyan + "Account is closed permanently.", End)
                print('\n')
                break
        else:
            print(Red + "User not found", End)
            print('\n')
    
    #Function to check the personal info:    
    def check_info():
        name_1 = input("Enter your name: ")
        govt_id_1 = int(input("Enter government issued id number: "))
        
        my_sql = "SELECT * FROM customer_info"
        cursor.execute(my_sql)
        information = cursor.fetchall()
        
        for column in information:
            name_check = column[0]
            age1 = column[1]
            gender1 = column[2]
            id_check = column[3]
            mob = column[4]
            bal = column[5]
            
            if name_1 == name_check and govt_id_1 == id_check:
                
                print(Yellow + f"""CUSTOMER DETAILS
                      Name: {name_check}
                      Age: {age1}
                      Gender: {gender1}
                      Government ID: {id_check}
                      Mobile Number: {mob}
                      Available Balance: {bal}
                      """, End)
                print('\n')
                break
        else:
            print(Red + "User not found", End)
            print('\n')
        
    while(True):
        
        print(Pink + """****** WELCOME ******
          1. Create Account
          2. Deposit
          3. Withdraw
          4. Check Balance
          5. Information
          6. Close Account
          7. Exit
          """, End)
        select = int(input("Enter your choice: "))
        
        match select:
            case 1:
                print(Blue + "Account Creation Process Begins... ", End)
                create_account()
                continue
            case 2: 
                print(Blue + "Deposit Process Begins... ", End)
                deposit()
                continue
            case 3: 
                print(Blue + "Withdraw Process Begins... ", End)
                withdraw()
                continue
            case 4: 
                print(Blue + "Checking Balance Process Begins... ", End)
                check_balance()
                continue
            case 5: 
                print(Blue + "Checking Information Process Begins... ", End)
                check_info()
                continue
            case 6: 
                print(Blue + "Account Closing Process Begins... ", End)
                close_account()
                continue
            case 7: 
                myconnection.close()
                sys.exit()
                       
mini_atm()
       