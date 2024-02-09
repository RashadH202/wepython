class CoffeeMachine:
    def __init__(self):
        self.profit = 0
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.MENU = {
            "expresso": {
                "ingredients": {"water": 50,  "coffee": 18}, 
                "cost":1.5,
            },
            "latte": {
                "ingredients": {"water": 200, "milk": 150, "coffee": 24}, 
                "cost":2.5,
            },
            "cappuccino": {
                "ingredients": {"water": 250, "milk": 100,  "coffee": 18}, 
                "cost":3.0,
            }
        }

    def print(self):
        """Prints rthe current resources and profit"""
        print(f"water: {self.resources['water']}ml")
        print(f"milk: {self.resources['milk']}ml")
        print(f"coffee: {self.resources['coffee']}ml")
        print(f"money: {self.profit}")

    def is_resource_sufficient(self, order_ingredients):
        """Return True when order can be made, False if ingredients aren't present"""
        for item in order_ingredients:
            if order_ingredients[item] > self.resources[item]:
                print(f"sorry there's not enough {item}.")
            return True
        
    def process_coins(self):
        """return the total calculated from coins inserted"""
        print("Please Insert Coins.")
        total = int(input("how many quaters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.10
        total += int(input("how many nickels?: ")) * 0.5
        total += int(input("how many pennies?: ")) * 0.1
        return total
    def is_transaction_successful(self, money_received, drink_cost):
        """return true when the pay is accepted, or false if money is too low"""
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change")
            self.profit += drink_cost
            return True
        else:
            print("Sorry you're broke??? here's your money back.")
            return False
        
    def make_coffee(self, drink_name, order_ingredients):
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is yor {drink_name} ☕️. Enjoy")

    def run(self):
        is_on=True
        while is_on:
            choice = self.get_user_choice()
            if choice == "off":
                is_on = False
            elif choice == "report":
                self.print_report()
            else:
                drink = self.Menu[choice]
                if self.is_resource_sufficient(drink["ingredients"]):
                    payment = self. process_coins()
                    if self.is_transaction_successful(payment,drink["cost"]):
                        self.make_coffee(choice, drink["ingredients"])

    def get_user_choice(self):
        """get user input for drink choice"""
        while True:
            choice = input("what would you like? (expresso, Latte, or Cappuccino)").lower()
            print("invalid choice. Please Choose a valid option!")
            if choice in {"expresso", "latte", "cappuccino", "off", "report"}:
                return choice
            else: 
                print("invalid choice, please choice again!")


"""Instance and run the cofee machine!"""
coffee_machine = CoffeeMachine()
coffee_machine.run() 

        

