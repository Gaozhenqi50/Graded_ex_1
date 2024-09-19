# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == 1:
        sorted_products = sorted(products_list, key=lambda x: x[1])
    else:
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
    
    display_products(sorted_products)
    return sorted_products


def display_products(products_list):
    for idx, (product, price) in enumerate(products_list, 1):
        print(f"{idx}. {product} - ${price}")


def display_categories():
    print("Categories available:")
    for idx, category in enumerate(products, 1):
        print(f"{idx}. {category}")


def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))
    print(f"{quantity} x {product[0]} added to cart.")


def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your cart contains:")
        total_cost = 0
        for idx, (product, price, quantity) in enumerate(cart, 1):
            print(f"{idx}. {product} - ${price} x {quantity} = ${price * quantity}")
            total_cost += price * quantity
        print(f"Total cost: ${total_cost}")
    return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- RECEIPT ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Delivery Address: {address}\n")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
    print(f"\nTotal cost: ${total_cost}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")


def validate_name(name):
    if len(name.split()) == 2 and all(part.isalpha() for part in name.split()):
        return True
    return False


def validate_email(email):
    if "@" in email:
        return True
    return False


def main():
    cart = []

    
    while True:
        name = input("Enter your name (First Last): ")
        if validate_name(name):
            break
        print("Invalid name. Please enter both first and last names using only alphabets.")

    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email. Please include an '@' in the email.")

    
    while True:
        display_categories()
        try:
            category_choice = int(input("\nEnter the category number you'd like to explore: "))
            if 1 <= category_choice <= len(products):
                category_name = list(products.keys())[category_choice - 1]
                category_products = products[category_name]
                
                while True:
                    print(f"\n{category_name} products:")
                    display_products(category_products)

                    print("\nOptions:")
                    print("1. Select a product to buy")
                    print("2. Sort products by price")
                    print("3. Go back to category selection")
                    print("4. Finish shopping")
                    choice = input("Choose an option: ")

                    if choice == "1":
                        product_choice = int(input("\nEnter the product number to buy: ")) - 1
                        if 0 <= product_choice < len(category_products):
                            product = category_products[product_choice]
                            quantity = int(input(f"Enter quantity for {product[0]}: "))
                            add_to_cart(cart, product, quantity)
                        else:
                            print("Invalid product number.")

                    elif choice == "2":
                        sort_order = int(input("\nSort by price: 1 for ascending, 2 for descending: "))
                        display_sorted_products(category_products, sort_order)

                    elif choice == "3":
                        break

                    elif choice == "4":
                        if cart:
                            total_cost = display_cart(cart)
                            address = input("Enter your delivery address: ")
                            generate_receipt(name, email, cart, total_cost, address)
                        else:
                            print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
                        return

                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid category number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# The following block ensures that main() function is called when the program is run directly
if __name__ == "__main__":
    main()

