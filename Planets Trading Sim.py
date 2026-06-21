import time
import json

planets=["earth", "venus", "mars", "mercury"]

#Reading Money
try:
    with open("itemData.json", "r") as dataFile:
        itemData=json.load(dataFile)
except:
    itemData={
"money":5000,
"Wood":0,
"Stone":0,
"Iron":0,
"Slamanium":0,
"currentPlanet":"earth"
}

#Writing Data
def data_saving():
    global itemData
    with open("itemData.json", "w") as dataFile:
        json.dump(itemData, dataFile)


ResourcePrice={

"earth":{
"Wood" : 690,
"Stone" : 440,
"Iron" : 510,
"Slamanium" : 1300},

"venus":{
"Wood" : 350,
"Stone" : 520,
"Iron" : 780,
"Slamanium" : 1350},

"mars":{
"Wood" : 290,
"Stone" : 320,
"Iron" : 980,
"Slamanium" : 1050},

"mercury":{
"Wood" : 500,
"Stone" : 210,
"Iron" : 450,
"Slamanium" : 1190}
}







while True:
    try:
        userInp=int(input("1. Travel\n2. Buy/Sell Goods\n3. Storage\n4. Current Planet\n"))
        
    except ValueError:
        print("Enter numbers only!!!")
        continue 
#Travelling to planets        
    if userInp==1:
            for planet in planets:
                print("\n",planet)
                
            try:
                travelInp=str(input("Enter Planet name:\n")).lower()
                
            except ValueError:
                print("Enter planet name only!!!")
                continue
                
            if travelInp in planets:
                if itemData["currentPlanet"] == travelInp:
                    print("You are already on",itemData["currentPlanet"]) 
                                     
                else:
                    
                    travelcfn=str(input("Travelling costs 150. Are you sure(y/n)"))
                    if travelcfn=="y":
                        print("\nTraveling...\n")
                        time.sleep(3)
                        itemData["currentPlanet"]=travelInp
                        itemData["money"]-=150
                        data_saving()
                    
            else:
                print("\nEnter planet names only!!\n")
    

#Buying And Selling Items
    elif userInp==2:
        try:
            tradeInp=int(input("\n1. Buy\n2. Sell\n"))
        except ValueError:
            print("Enter numbers only!!!")
        if tradeInp==1:
            print("What do you want to buy?\n")
            for items, prices in ResourcePrice[itemData["currentPlanet"]].items():
                print(items,":",prices)
            try:
                buyInp=str(input("What do you want to buy?\n"))
            except ValueError:
                print("Enter what is given above!!!")
                continue
                
            if buyInp in ResourcePrice[itemData["currentPlanet"]]:
                try:
                    buyAmount=int(input("How many?: "))
                except ValueError:
                    print("Enter numbers!!")
                    continue
                buyPrice=ResourcePrice[itemData["currentPlanet"]][buyInp]*buyAmount
                print(buyPrice)
                if buyPrice<=itemData["money"]:
                    itemData["money"] -= buyPrice
                    itemData[buyInp]+=buyAmount
                    data_saving()
                else:
                    print("Not enough money!!")
                        

        elif tradeInp==2:
            print("Items in your storage:-")
            for item, data in itemData.items():
                if item!="currentPlanet":
                    print(item,":",data)
        
            try:
                sellInp=str(input("What do you want to sell?: "))
            except ValueError:
                print("Enter items name only!!!")
                continue
            try:
                sellAmount=int(input("How many?: "))
            except ValueError:
                print("Enter Amount!!!")
                continue
                
            if itemData[sellInp] != 0:
                if sellInp=="Stone":
                    if sellAmount>itemData[sellInp]:
                        print("\nNot enough!!")
                    elif sellAmount<=itemData[sellInp]:
                        itemData["money"]+=200*sellAmount
                        itemData[sellInp]-=sellAmount
                        print("\nSold for",sellAmount*200,"\n")
                        data_saving()
                
                
                
                if sellInp=="Wood":
                    if sellAmount>itemData[sellInp]:
                        print("\nNot enough!!")
                    elif sellAmount<=itemData[sellInp]:
                        itemData["money"]+=150*sellAmount
                        itemData[sellInp]-=sellAmount
                        print("\nSold for",sellAmount*150,"\n")
                        data_saving()
                        
                if sellInp=="Iron":
                    if sellAmount>itemData[sellInp]:
                        print("\nNot enough!!")
                    elif sellAmount<=itemData[sellInp]:
                        itemData["money"]+=370*sellAmount
                        itemData[sellInp]-=sellAmount
                        print("\nSold for",sellAmount*370,"\n")
                        data_saving()
                       
                if sellInp=="Slamanium":
                   if sellAmount>itemData[sellInp]:
                        print("\nNot enough!!")
                   elif sellAmount<=itemData[sellInp]:
                        itemData["money"]+=500*sellAmount
                        itemData[sellInp]-=sellAmount
                        print("\nSold for",sellAmount*500,"\n")
                        data_saving()
                
            else:
                print("\nPsych, you are poor!!\n")

    elif userInp==3:
        print("Items in your storage:-")
        for item, data in itemData.items():
            if item!="currentPlanet":
                print(item,":",data,"\n")
            
            
    elif userInp==4:
        print("\nRight now you are on",itemData["currentPlanet"])     