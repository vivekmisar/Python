class coffeeshop:

    def __init__(self):
        
        self.menu = {
            #dictionary
            "espresso":50,
            "latte":100,
            "cappuccino":60,
            "americano":40,
            "mocha":80,
        }
    
        self.inventory = {
            "espresso":10,
            "latte":10,
            "cappuccino":10,
            "americano":10,
            "mocha":10
        }


        self.sales = 0.0

    def display_menu(self):
        
        print("\n------Menu------")

        for item,price in self.menu.items():
            print(f"{item.capitalize()}:₹{price:.2f}")

        print("------------------\n")

    def take_order(self):
        self.display_menu()

        order = input("What would you like to order : ").lower()

        if order in self.menu:
            
            if self.inventory[order]>0:

                quantity = int(input("How many would you like to purchase (enter no.of quantity) : "))

                if quantity <= self.inventory[order]:

                    self.process_order(order,quantity)

                else:

                    print(f"Sorry,we are out of the {order}")

            else:

                print("Sory,We don't have that item on the menu.")

    def process_order(self,order,quantity):

        cost = self.menu[order] * quantity

        print(f"Your order : {quantity} {order}(s) for ₹{cost:.2f}")

        confirm = input("Would you like to proceed with order (yes/no)? : ").lower()
        
        if confirm == "yes":

            self.sales += cost
            self.inventory[order] -= quantity

            print(f"Thank you, your order for {quantity} {order}(s) has been placed.")

        else:
            print("Order canceled.")

    def display_sales(self):
        print(f"\n Total Sales: ₹{self.sales:.2f}")


    def dislpay_inventory(self):

        print("\n-----Inventory-----")

        for item,quantity in self.inventory.items():

            print(f"{item.capitalize()}:{quantity}")

        print("----------------------\n")

# user interaction
def main():

    shop = coffeeshop()
#creation of user interaction menu

    while True :
        print("\nWelcome to the Coffee Shop Management System")
        print("1. Place an order.")
        print("2. view Sales")
        print("3. view Inventory")
        print("4. Exit")

        choice = input("Please Select an option: ")


        if choice == "1":
            
            shop.take_order()

        elif choice == "2":

            shop.display_sales()

        elif choice == "3":

            shop.dislpay_inventory()

        elif choice == "4":
            
            print("Thank you for using the Coffee Shop Management System. Good BYE!!\n")
            break

        else:

            print("Invalid choice , Please select a valid option.")


if __name__ == "__main__":
     main()

