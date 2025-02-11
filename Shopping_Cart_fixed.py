# I have added the functionality to input any quantity of each item in the action number 1. I have added also the correspondig computed amount according to quantities when they are displayed in action 2 or 3 and the whole total in action 4.
# Author: Carlos Enrique Guardado Cruz.
print("Welcome to the Shopping Cart Program!")

items_quantity = []
cart_items = []
prices = []
subtotals = []
quantity = 0
item = ""
price = 0
user_selection = 0
while user_selection != 5:
    print()
    print("Please select one of the following: ")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute total")
    print("5. Quit")
    user_selection = int(input("Please enter an action: "))
    
    if user_selection == 1:
            item = str(input("What item would you like to add? "))
            quantity = int(input(f"How many '{item}'? "))
            price = float(input(f"What is the price of '{item}'? "))



            cart_items.append(item)
            items_quantity.append(quantity)
            prices.append(price)
            subtotals.append(quantity * price)

            print(f"'{item}' has been added to the cart")

    elif user_selection == 2:
            print("The contents of the shopping cart are:")
            for n, q, i, p, st in zip(range(len(cart_items)), items_quantity, cart_items, prices, subtotals):
                    print(f"{n + 1}. {q} {i} - ${p:.2f} ---> ${st:.2f}")

    elif user_selection == 3:
            print("The contents of the shopping cart are:")
            for n, q, i, p, st in zip(range(len(cart_items)), items_quantity, cart_items, prices, subtotals):
                    print(f"{n + 1}. {q} {i} - ${p:.2f} ---> ${st:.2f}")
            print()
            remove_selection = int(input("Which item would you like to remove? "))
            if remove_selection <= len(cart_items):
                n = 0
                for n in range(len(cart_items)):
                    if n == remove_selection - 1:
                        cart_items.pop(n)
                        items_quantity.pop(n)
                        prices.pop(n)
                        subtotals.pop(n)
                        print("Item removed")
            else:
                print("Sorry, that is not a valid item number.")
                
    elif user_selection == 4:
        total = sum(subtotals)   
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
                       
print("Thank you. Good bye.")