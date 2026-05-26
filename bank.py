try:
    with open("money.txt", "r") as Moneyfile:
        money=int(Moneyfile.read())
        Moneyfile.read(money)
except FileNotFoundError:
    print("File Not Found")
    money=10000
    
#Saving Money
def money_saving():
    with open("money.txt", "w") as Moneyfile:
        Moneyfile.write(str(money))
       
          
try:
    with open("bank.txt", "r") as Bankfile:
        bank=int(Bankfile.read())
except FileNotFoundError:
    print("File Not Found")
    bank=0
    
#Saving wallet
def bank_saving():
    with open("bank.txt", "w") as Bankfile:
        Bankfile.write(str(bank))   
        
        
        
        
while True:        
    try:
        userInp=int(input("1. Deposit Money\n2. Withdraw Money\n3. Wallet\n4. Bank\n5. Exit\n"))
    except ValueError:
        print("Enter numbers only!!")
    
    if userInp==1:
        try:
            deposit=int(input("\nHow much do you want to deposit?:\n"))
        except ValueError:
            print("Enter numbers only!!")
            continue
    
        if deposit>money or deposit<0::
            print("Not enough money or enter positive numbers!!")
        elif deposit<=money:
            bank+=deposit
            money-=deposit
            print("Deposited",deposit)
            bank_saving()
            money_saving()
    
    elif userInp==2:
        try:
            withdraw=int(input("\nHow much do you want to withdraw:\n"))
        except ValueError:
            print("Enter numbers only!!\n")
            continue
        
        if withdraw>bank:
            print("\nNot enough money in bank!!")
        elif withdraw<=bank:
            money+=withdraw
            bank-=withdraw
            print("\nWithdrawed",withdraw)
            bank_saving()
            money_saving()
    
    elif userInp==3:
        print("\n",money,"\n")
        
    elif userInp==4:
        print("\n",bank,"\n")
    
    elif userInp==5:
        break