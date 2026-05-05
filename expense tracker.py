import json

try:
    with open("expense.json", "r") as file:
        data=json.load(file)
except:
    data={}

while True:
    print("\n")
    print("1. Add expense\n2. See expense\n3. Delete all expense\n4. Show total:")
    userInp=int(input("Enter your choice: "))
    if userInp==1:
        print("\n")
        expenseNa=input("Enter expense name: ")
        expense=int(input("Enter its price: ")) 
        data[expenseNa]=expense
        with open("expense.json", "w") as file:
            json.dump(data, file)
    elif userInp==2:
        if data=={}:
            print("Nothing here.")
        else:
            print("All expenses:")
            for name, price in data.items():
                print(name,":",price)
    elif userInp==3:
        if data=={}:
            print("Nothing here.")
        else:
            print("All expenses:")
            for name, price in data.items():
                print(name,":",price)
            print("Enter what you wanna delete:")
            exDel=input("")
            if exDel in data:
                del data[exDel]
                print("Deleted",exDel)
                with open("expense.json", "w") as file:
                    json.dump(data, file)
            else:
                print("Didn't found",exDel)
    elif userInp==4:
        total=sum(data.values())
        print(total)