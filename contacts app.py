import json

try:
    with open("cont.json", "r") as file:
        data=json.load(file)
except:
    data={}

while True:
    print("\n")
    print("1. Add contact\n2. See contacts\n3. Delete contacts\n4. Search contacts")
    userInp=int(input("Enter your choice: "))
    if userInp==1:
        print("\n")
        addNo=int(input("Enter number: "))
        addNa=input("Enter name: ")
        if addNa in data:
            print("Name already in list")
        else:
            data[addNa] = addNo
        with open("cont.json", "w") as file:
            json.dump(data, file)
        
    
    elif userInp==2:
        print("\n")
        
        if data=={}:
            print("Nothing in contacts.")
        else:
            for name, number in data.items():
                print(name,":",number)
        print("\n")
        
    elif userInp==3:
        print("Contacts:")
        for name, number in data.items():
            print(name,":",number)
        print("\n")
        delCont=input("Enter name of the contact to delete: ")
        if delCont in data:
            del data[delCont]
            with open("cont.json", "w") as file:
                json.dump(data, file)
        else:
            print("No contact with such name")
            
    elif userInp==4:
        print("Search a contact by typing its name")
        search=input("")
        if search in data:
            print("Number is",data[search])
        else:
            print("No contact found")