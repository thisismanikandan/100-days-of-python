game_is_on = True

resources = {
    'water' : 1000,
    'milk' : 1000,
    'coffee' : 500,
    'money' : 0
}

while game_is_on:
    choice = input("\nWhat would you like? (espresso/ latte/ cappucino): ")

    def update_resource(choice):
        if choice == "espresso":
            resources["water"] -= 50
            resources["coffee"] -= 18

        elif choice == "latte":
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150

        elif choice == "cappucino":
            resources["water"] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100

    # # coins
    # penny = 1 cent = $0.01
    # nickel = 5 cents = $0.05
    # dime = 10 cents = $0.1
    # quarter = 25 cents = $0.25

    # # espresso $1.50
    # 50ml water
    # 18g coffee

    # # latte $2.50
    # 200ml water
    # 24g coffee
    # 150ml milk

    # # cappucino $3.00
    # 250ml water
    # 24g coffee
    # 100ml milk

    def check_balance(total):
        if choice == "espresso":
            if total > 1.5:
                balance = total - 1.5
                balance = round(balance, 2)
                print(f"Here is ${balance} in change!")
                return balance
            elif total == 1.5:
                return
            else: 
                process_coins()
        if choice == "latte":
            if total > 2.5:
                balance = total - 2.5
                balance = round(balance, 2)
                print(f"Here is ${balance} in change!")
                return balance
            elif total == 2.5:
                return
            else: 
                process_coins()
        if choice == "cappucino":
            if total > 3:
                balance = total - 3
                balance = round(balance, 2)
                print(f"Here is ${balance} in change!")
                return balance
            elif total == 3:
                return
            else: 
                process_coins()
        

    def process_coins():
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = pennies*0.01 + nickles*0.05 + dimes*0.1 + quarters*0.25
        balance = check_balance(total)
        resources["money"] += total - balance


    def check_resource(choice):
        if choice == "espresso":
            if resources["water"] > 50:
                if resources["coffee"] > 18:
                    print("\nEnter coins\n ")
                    process_coins()
                    print("Here is your espresso, Enjoy !!!")
                    update_resource(choice)
                    print(resources)
                else:
                    print("\nSorry, there is no enough coffee")
            else:
                print("\nSorry, there is no enough water")
        if choice == "latte":
            if resources["water"] > 200:
                if resources["coffee"] > 24:
                    if resources["milk"] > 150:
                        print("\nEnter coins\n ")
                        process_coins()
                        print("Here is your latte, Enjoy !!!")
                        update_resource(choice)
                        print(resources)
                    else:
                        print("\nSorry, there is no enough milk")
                else:
                    print("\nSorry, there is no enough coffee")
            else:
                print("\nSorry, there is no enough water")
        if choice == "cappucino":
            if resources["water"] > 250:
                if resources["coffee"] > 24:
                    if resources["milk"] > 100:
                        print("\nEnter coins\n ")
                        process_coins()
                        print("Here is your cappucino, Enjoy !!!")
                        update_resource(choice)
                        print(resources)
                    else:
                        print("\nSorry, there is no enough milk")
                else:
                    print("\nSorry, there is no enough coffee")
            else:
                print("\nSorry, there is no enough water")

    if choice == "report":
        print(resources)
    else:
        check_resource(choice)


