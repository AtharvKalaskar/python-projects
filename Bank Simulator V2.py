import json
import os
import time
import threading
                

#Reading Account Data
try:
    with open("account.json", "r") as accFile:
        accData=json.load(accFile)
except:
    accData={}

#Writing Account Data
def acc_saving():
    with open("account.json", "w") as accFile:
        json.dump(accData, accFile)
        
        
def interest_system():
    while True:
        for user in accData.keys():
            interest=int(accData[user]["deposit"] * 0.01)
            if interest>0:
                accData[user]["deposit"]+=interest 
        acc_saving()
        time.sleep(60)


loginBool=False
interest_thread = threading.Thread(
    target=interest_system,
    daemon=True
)
interest_thread.start()
while True:
    if loginBool==False:
        print("\n1. Login\n2. Create Account\n3. Exit\n4. Clear Screen\n")
        try:
            loginInp=int(input("Enter your choice:\n"))
        except ValueError:
            print("Enter numbers only!!")
            continue
   
#Login System
        if loginInp==1:
            username=input("\nEnter your user name:\n")
            userPass=input("\nEnter your password:\n")
            if username in accData:
                if userPass == accData[username]["password"]:
                    print("Welcome",username)
                    loginBool=True
                else:
                    print("Wrong username or password")
            
            else:
                print("No user with such name!!")
            
    
#Create Account System
        elif loginInp==2:
            username=input("\nEnter your user name:\n")    
            userPass=input("Enter your password:\n")
       
            if username not in accData:
                accData[username]={
            "password":userPass,
            "balance":100,
            "deposit":0,
            "last_interest":time.time()}
                print("Account Created!")
                acc_saving()
                loginBool=True
                
            else:
                print("Username Taken!")
        elif loginInp==3:
                break
                
        elif loginInp==4:
            os.system('cls' if os.name == 'nt' else 'clear') 
        else:
                print("\nYou have only 4 options\n")
                
    elif loginBool==True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Check Deposit\n5. Log out\n6. Clear Screen\n")
           
        try: 
              userInp=int(input("Enter your choice:\n"))
        except ValueError:
              print("Enter in numbers only!!\n")
              continue
              
#Depositing Money            
        if userInp==1:
            try:
                deposit=int(input("\nEnter how much do you want to deposit:\n"))
            except ValueError:
                print("Enter in numbers only!!")
                continue
                
            if deposit<0:
                print("Nah bro you cant fool me!!")
                continue
            else:
                
                if deposit>accData[username]["balance"]:
                  print("Not enough money")
                else:
                    print("Deposited",deposit)
                    accData[username]["balance"]-=deposit
                    accData[username]["deposit"]+=deposit
                    acc_saving()
#Withdrawing Money
        elif userInp==2:
            try:
                withdraw=int(input("\nHow much do you want to withdraw?:"))
            except ValueError:
                print("\nEnter numbers only!!")
                continue
            
            if withdraw<0:
                print("Nah bro you cant fool us!!")
            else:
                
                if withdraw>accData[username]["deposit"]:
                    print("\nNot enough money in bank!!")
                else:
                    accData[username]["balance"]+=withdraw
                    accData[username]["deposit"]-=withdraw
                    acc_saving()
                    print("\nWithdrew",withdraw)    
#Money in bank        
        elif userInp==3:
            print("\nYour Balance:",accData[username]["balance"])
#Your balance        
        elif userInp==4:
            print("\nYou have deposited:",accData[username]["deposit"])
#Loging Out
        elif userInp==5:
            loginBool=False
            print("\nLogged out!\n")
            
        elif userInp==6:
            os.system('cls' if os.name == 'nt' else 'clear')
        
        else:
            print("\nYou have only 6 options!!\n")