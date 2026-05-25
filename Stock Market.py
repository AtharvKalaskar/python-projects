import random
import time
import threading
import os

ramPrice=2000

ramAmount=0

#Reading Money Data
try:
    with open("money.txt", "r") as Moneyfile:
        money=int(Moneyfile.read())
        Moneyfile.read(money) 
except FileNotFoundError:
    print("File Not Found")
    money=10000
    
#Saving Money
def money_saving():
    global money
    with open("money.txt", "w") as Moneyfile:
        Moneyfile.write(str(money))
       
#Reading ram data       
try:
    with open("ram.txt", "r") as Ramfile:
        ramAmount=int(Ramfile.read())
        Ramfile.read(ramAmount) 
except FileNotFoundError:
    print("File Not Found")
    ramAmount=0
    
#Saving Ram
def ram_saving():
    global ramAmount
    with open("ram.txt", "w") as Ramfile:
        Ramfile.write(str(ramAmount))



#Random Prices
def PriceUp():
    global ramPrice
    ramPrice+=random.randint(10, 50)

def PriceDown():
    global ramPrice
    ramPrice-=random.randint(10, 40)
    if ramPrice<100:
        ramPrice=100

def market_engine():
    functions = [PriceUp, PriceDown]
    while True:
        random.choice(functions)()
        time.sleep(2)

threading.Thread(target=market_engine, daemon=True).start()


while True:
    userInp=int(input("1. See Price\n2. Buy/Sell RAM\n3. See Money and RAM\n4. Clear Screen:\n"))
    if userInp==1:
        print(ramPrice)
    
    elif userInp==2:
        print("\n1. Buy RAM\n2. Sell RAM:\n")
        ramInp=int(input(""))
        if ramInp==1:
            cfn=input("Are you sure you want to buy RAM(y/n):\n")
            if cfn=="y":
                if money>=ramPrice:
                    money-=ramPrice
                    ramAmount+=1
                    print(money)
                    print(ramAmount)
                    money_saving()
                    ram_saving()
                else:
                    print("Not enough money!")
                    
            elif cfn=="n":
                print("Cancelled")
        
        elif ramInp==2:
            sellAmount=int(input("Enter how much you want you sell: "))
            if ramAmount<sellAmount:
                print("You don't enough have RAM!!")
            else:
                money += sellAmount*ramPrice
                ramAmount-=sellAmount
                print("You sold you ram!")
                money_saving()
                ram_saving()
        
    elif userInp==3:
            print("\nYou have",money)
            print("You have",ramAmount,"RAM\n")
            
    elif userInp==4:
        os.system('cls' if os.name == 'nt' else 'clear')
