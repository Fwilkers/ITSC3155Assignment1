### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        breadCost = self.machine_resources['bread'] - ingredients['ingredients']['bread']
       # print(breadCost)
        hamCost = self.machine_resources['ham'] - ingredients['ingredients']['ham']
       # print(hamCost)
        cheeseCost = self.machine_resources['ham'] - ingredients['ingredients']['cheese']
       # print(cheeseCost)
        if (breadCost <= 0):
            print("Not enough bread for this order. Please restock")
            return False
        if (hamCost <= 0):
            print("Not enough ham for this order. Please restock")
            return False
        if (cheeseCost <= 0):
            print("Not enough cheese for this order. Please restock")
            return False
        return True
        """Returns True when order can be made, False if ingredients are insufficient."""

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        money = 0.00
        dollars = input("How many dollars? ")
        d = float(dollars)
        money = money + d
        #print(money)
        half = input("How many half-dollars? ")
        h = float(half)
        money = money + (h * .5)
        #print(money)
        quarters = input("How many quarters? ")
        q = float(quarters)
        money = money + (q * .25)
        #print(money)
        nickels = input("How many nickels? ")
        n = float(nickels)
        money = money + (n * .05)
        print("You entered $", money)
        return money

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##print(coins, cost)
        if coins >= cost:
            return True
        if coins < cost:
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources['bread'] = self.machine_resources['bread'] - order_ingredients['bread']
        self.machine_resources['ham'] = self.machine_resources['ham'] - order_ingredients['ham']
        self.machine_resources['cheese'] = self.machine_resources['cheese'] - order_ingredients['cheese']


### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwichMachine = SandwichMachine(resources);
on = True;
canMake = False;

while on == True:
    inpt = input("What would you like? small/medium/large? Type 'resources' to view current resources, 'off' to turn program off ")
    if inpt == "small":
        print("You chose small")
        canMake = sandwichMachine.check_resources(recipes["small"])
        if canMake:
            payment = sandwichMachine.process_coins()
            cost = recipes["small"]["cost"]
            #print(cost)
            coversCost = sandwichMachine.transaction_result(payment, recipes["small"]["cost"])
            if coversCost:
                sandwichMachine.make_sandwich("small", recipes["small"]["ingredients"])
                print("That comes out to $", payment - cost, " in change")
                print("Your small sandwich is ready. Bon appetit!")
            if coversCost == False:
                print("You don't have enough money")
    if inpt == "medium":
        print("You chose medium")
        canMake = sandwichMachine.check_resources(recipes["medium"])
        if canMake:
            payment = sandwichMachine.process_coins()
            cost = recipes["medium"]["cost"]
            coversCost = sandwichMachine.transaction_result(payment, recipes["medium"]["cost"])
            if coversCost:
                sandwichMachine.make_sandwich("medium", recipes["medium"]["ingredients"])
                print("That comes out to $", payment - cost, " in change")
                print("Your medium sandwich is ready. Bon appetit!")
            if coversCost == False:
                print("You don't have enough money")
    if inpt == "large":
        print("You chose large")
        canMake = sandwichMachine.check_resources(recipes["large"])
        if canMake:
            payment = sandwichMachine.process_coins()
            cost = recipes["large"]["cost"]
            coversCost = sandwichMachine.transaction_result(payment, recipes["large"]["cost"])
            if coversCost:
                sandwichMachine.make_sandwich("large", recipes["large"]["ingredients"])
                print("That comes out to $", payment - cost, " in change")
                print("Your large sandwich is ready. Bon appetit!")
            if coversCost == False:
                print("You don't have enough money")
    if inpt == "resources":
        print("Bread: ", sandwichMachine.machine_resources["bread"])
        print("Ham: ", sandwichMachine.machine_resources["ham"])
        print("Cheese: ", sandwichMachine.machine_resources["cheese"])
    if inpt == "off":
        on = False
