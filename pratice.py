# Mini Shopping System
# Covers Python Day 1 to Day 10 Concepts

print("=== Welcome to Mini Shopping System ===")

# Product dictionary (Day 10)
products = {
    "rice": 50,
    "milk": 30,
    "bread": 40,
    "eggs": 6,
    "oil": 120
}

# Cart list (Day 7)
cart = []

while True:

    print("\nMenu")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Calculate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # View Products
    if choice == "1":

        print("\nAvailable Products:")

        # Loop (Day 5)
        for item in products:

            print(item, "- Rs.", products[item])

    # Add to Cart
    elif choice == "2":

        item = input("Enter product name: ").lower()

        if item in products:

            qty = int(input("Enter quantity: "))

            price = products[item]

            total_price = price * qty

            # Tuple (Day 9)
            cart_item = (item, qty, total_price)

            cart.append(cart_item)

            print("Item added to cart!")

        else:

            print("Product not available.")

    # View Cart
    elif choice == "3":

        if len(cart) == 0:

            print("Cart is empty.")

        else:

            print("\nYour Cart:")

            for item in cart:

                print("Product:", item[0])
                print("Quantity:", item[1])
                print("Total Price:", item[2])
                print("---------------------")

    # Calculate Bill
    elif choice == "4":

        if len(cart) == 0:

            print("Cart is empty.")

        else:

            total_bill = 0

            for item in cart:

                total_bill = total_bill + item[2]

            print("\nTotal Bill Amount: Rs.", total_bill)

            # Discount condition
            if total_bill > 500:

                discount = total_bill * 0.10
                final_amount = total_bill - discount

                print("Discount Applied: Rs.", discount)
                print("Final Amount: Rs.", final_amount)

            else:

                print("No discount applied.")

    # Exit
    elif choice == "5":

        print("Thank you for shopping!")
        break

    else:

        print("Invalid choice. Try again.")
