def main():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    import art
    from art import logo
    import os
    print(logo)

    money=0
    def reporting(resources, money):
        print(f"Water: {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Milk : {resources['coffee']}g")
        print(f"Money: ${money}")

    #Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    #a. Check the user’s input to decide what to do next.
    #b. The prompt should show every time action has completed, e.g. once the drink is
    #dispensed. The prompt should show again to serve the next customer.
    def working(money):
        prompt=input("\n What would you like? (espresso/latte/cappuccino)")

        ## Turn off the Coffee Machine by entering “off” to the prompt.
        ## a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        ## the machine. Your code should end execution when this happens

        if prompt=="off":
            exit("Have a nice day")
        #Print report.
        #a. When the user enters “report” to the prompt, a report should be generated that shows
        #the current resource values. e.g.
        #Water: 100ml
        #Milk: 50ml
        #Coffee: 76g
        #Money: $2.5

        elif prompt=="report":
            reporting(resources,money)

            #4. Check resources sufficient?
        #a. When the user chooses a drink, the program should check if there are enough
        #resources to make that drink.
        #b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
        #not continue to make the drink but print: “Sorry there is not enough water.”
        #c. The same should happen if another resource is depleted, e.g. milk or coffee.
        #5. Process coins.
        #a. If there are sufficient resources to make the drink selected, then the program should
        #prompt the user to insert coins.
        #b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        #c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        #pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
        #6. Check transaction successful?
        #a. Check that the user has inserted enough money to purchase the drink they selected.
        #E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        #program should say “Sorry that's not enough money. Money refunded.”.
        #b. But if the user has inserted enough money, then the cost of the drink gets added to the
        #machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        #Water: 100ml
        #Milk: 50ml
        #Coffee: 76g
        #Money: $2.5
        #c. If the user has inserted too much money, the machine should offer change.
        #E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
        #places.

        transaction=0  #for checking transaction... if enough $ in machine it is set to 1,2 or 3, if respectively buying 1=CAPPUCCINO, 2=LATTE, 3=ESPRESSO

        def coins(drink_value):
            print("Please insert coins: ")
            quarters=int(input("How many quarters?: ")) #quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            dimes=int(input("How many dimes?: "))
            nickles=int(input("How many nickles?: "))
            pennies=int(input("How many pennies?: "))

            inserted_coins=quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
            if drink_value>inserted_coins:
                print("Sorry that's not enough money. Money refunded.")
                return 0
            elif drink_value<inserted_coins:
                change=round(inserted_coins-drink_value,2)
                print(f"Here is ${change} in change.")
                return drink_value
            else:
                return drink_value

        if prompt=="cappuccino":
            if MENU["cappuccino"]["ingredients"]["water"]>resources["water"]:
                print("Sorry there is not enough water.")
                working(money)
            elif MENU["cappuccino"]["ingredients"]["milk"]>resources["milk"]:
                print("Sorry there is not enough milk.")
                working(money)
            elif MENU["cappuccino"]["ingredients"]["coffee"]>resources["coffee"]:
                print("Sorry there is not enough coffee.")
                working(money)
            else:
                money+=coins(MENU["cappuccino"]["cost"])
                transaction=1

        elif prompt=="latte":
            if MENU["latte"]["ingredients"]["water"]>resources["water"]:
                print("Sorry there is not enough water.")
                working(money)
            elif MENU["latte"]["ingredients"]["milk"]>resources["milk"]:
                print("Sorry there is not enough milk.")
                working(money)
            elif MENU["latte"]["ingredients"]["coffee"]>resources["coffee"]:
                print("Sorry there is not enough coffee.")
                working(money)
            else:
                money+=coins(MENU["latte"]["cost"])
                transaction=2
        elif prompt=="espresso":
            if MENU["espresso"]["ingredients"]["water"]>resources["water"]:
                print("Sorry there is not enough water.")
                working(money)
            elif MENU["espresso"]["ingredients"]["coffee"]>resources["coffee"]:
                print("Sorry there is not enough coffee.")
                working(money)
            else:
                money+=coins(MENU["espresso"]["cost"])
                transaction=3


        #7. Make Coffee.
        #a. If the transaction is successful and there are enough resources to make the drink the
        #user selected, then the ingredients to make the drink should be deducted from the
        #coffee machine resources.
        #E.g. report before purchasing latte:
        #Water: 300ml
        #Milk: 200ml
        #Coffee: 100g
        #Money: $0
        #Report after purchasing latte:
        #Water: 100ml
        #Milk: 50ml
        #Coffee: 76g
        #Money: $2.5
        #b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
        #latte was their choice of drink.

        if transaction==1:
            resources["water"]-=MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"]-=MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"]-=MENU["cappuccino"]["ingredients"]["coffee"]
            print("Here is your cappuccino. Enjoy!")
            working(money)
        elif transaction==2:
            resources["water"]-=MENU["latte"]["ingredients"]["water"]
            resources["milk"]-=MENU["latte"]["ingredients"]["milk"]
            resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"]
            print("Here is your latte. Enjoy!")
            working(money)
        elif transaction==3:
            resources["water"]-=MENU["espresso"]["ingredients"]["water"]
            resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
            print("Here is your espresso. Enjoy!")
            working(money)

    working(money)
   # _= os.system('cls')
   

main()