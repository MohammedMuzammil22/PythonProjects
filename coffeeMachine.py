def getCoin():
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))
    quarters = 0.25*q
    dimes = 0.10*d
    nickles = 0.05*n
    pennies = 0.01*p
    total = quarters + dimes + nickles + pennies
    return total


def validateCoin(total,requiredAmount,user_choice):
    if(total<requiredAmount):
        print("Sorry thats not enough money. Money refunded!")
        return True
    else:
        amt,type = requirements(user_choice)
        change = total - amt
        print(f"Here is ${change} in change.")


def updateReport(coffeeType,water,milk,coffee,requiredAmount,money):
    if(coffeeType.lower() == "espresso" and water>=50 and coffee>=18):
        water-=50
        coffee-=18
        money += requiredAmount
        return(water,milk,coffee,requiredAmount,money)
    elif(coffeeType.lower() == "latte" and water>=200 and coffee>=24 and milk>=150):
        water-=200
        coffee-=24
        milk-=150
        money += requiredAmount
        return(water,milk,coffee,requiredAmount,money)
    elif(coffeeType.lower() == "cappuccino" and water>=250 and coffee>=24 and milk>=100):
        water-=250
        coffee-=24
        milk-=100
        money += requiredAmount
        return(water,milk,coffee,requiredAmount,money)
    else:
        print("Sorry there is not enough water.")
        return(-1,-1,-1,-1,-1)


def requirements(user_choice):
    if(user_choice.lower()=='a'):
        return (1.5,"espresso")
    elif(user_choice.lower()=='b'):
        return (2.5,"latte")
    elif(user_choice.lower()=='c'):
        return (3.0,"cappuccino")


def printReport(water,milk,coffee,money):
    print(f"Available Items are :-")
    print(f"Water = {water}ml")
    print(f"Milk = {milk}ml")
    print(f"Coffee = {coffee}g")
    print(f"Money = ${money}")
    

water= 500
milk= 350
coffee= 100
money= 0
while(True):
    while(True):
        user_choice = input("""What would you like? select the option
a.espresso
b.latte
c.cappuccino
choice: """)
        if(user_choice.lower()=='a' or user_choice.lower()=='b' or user_choice.lower()=='c' or user_choice.lower()=='report' or user_choice.lower()=='off'):
            break
        else:
            print("Select the appropriate option (a/b/c): ")
    
    if(user_choice.lower()=='off'):
        break
    elif(user_choice.lower()=='report'):
        printReport(water,milk,coffee,money)
        continue 
    requiredAmount,coffeeType = requirements(user_choice)
    check=updateReport(coffeeType,water,milk,coffee,requiredAmount,money)
    if(check[0]==-1):
        continue
    total = getCoin()
    notvalid = validateCoin(total,requiredAmount,user_choice)
    if(notvalid ==True):
        continue
    else:
        water,milk,coffee,requiredAmount,money=updateReport(coffeeType,water,milk,coffee,requiredAmount,money)
        print(f"Here is your {coffeeType} enjoy! ")
        




