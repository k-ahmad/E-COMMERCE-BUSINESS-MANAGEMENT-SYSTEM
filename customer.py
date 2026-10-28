
from admin import products


def view_customer_products():
    print("\n========== AVAILABLE PRODUCTS ==========")

    if not products:
        print("No products are available right now.")
        return

    for product_id, product in products.items():
        if product["quantity"] > 0:
            print(f"\nID: {product_id}")
            print(f"Name: {product['name']}")
            print(f"Price: Rs. {product['price']:.2f}")
            print(f"Available stock: {product['quantity']}")


def search_customer_product():
    print("\n========== SEARCH PRODUCTS ==========")

    keyword = input("Enter product name: ").strip().lower()
    found = False

    for product_id, product in products.items():
        if keyword in product["name"].lower():
            if product["quantity"] > 0:
                print(
                    f"ID: {product_id} | "
                    f"Name: {product['name']} | "
                    f"Price: Rs. {product['price']:.2f} | "
                    f"Stock: {product['quantity']}"
                )
                found = True

    if not found:
        print("No matching available product found.")


def add_to_cart(cart):
    print("\n========== ADD TO CART ==========")

    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    if product_id not in products:
        print("Product not found!")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return

    product = products[product_id]
    already_in_cart = cart.get(product_id, 0)

    if already_in_cart + quantity > product["quantity"]:
        print("Sorry! Not enough stock available.")
        return

    cart[product_id] = already_in_cart + quantity

    print(f"{product['name']} added to your cart!")


def view_cart(cart):
    print("\n========== YOUR SHOPPING CART ==========")

    if not cart:
        print("Your cart is empty.")
        return

    total = 0

    for product_id, quantity in cart.items():
        product = products.get(product_id)

        if product is None:
            continue

        subtotal = product["price"] * quantity
        total += subtotal

        print(f"\nProduct: {product['name']}")
        print(f"Quantity: {quantity}")
        print(f"Subtotal: Rs. {subtotal:.2f}")

    print("-" * 35)
    print(f"Cart Total: Rs. {total:.2f}")


def remove_from_cart(cart):
    print("\n========== REMOVE FROM CART ==========")

    if not cart:
        print("Your cart is empty.")
        return

    view_cart(cart)

    try:
        product_id = int(input("\nEnter product ID to remove: "))
    except ValueError:
        print("Invalid product ID!")
        return

    if product_id in cart:
        del cart[product_id]
        print("Product removed from cart!")
    else:
        print("That product is not in your cart.")


def customer_panel(user):
    cart = {}

    while True:
        print("\n========== CUSTOMER PANEL ==========")
        print(f"Welcome, {user['name']}!")
        print("1. View Products")
        print("2. Search Products")
        print("3. Add Product to Cart")
        print("4. View Cart")
        print("5. Remove Product from Cart")
        print("6. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_customer_products()

        elif choice == "2":
            search_customer_product()

        elif choice == "3":
            add_to_cart(cart)

        elif choice == "4":
            view_cart(cart)

        elif choice == "5":
            remove_from_cart(cart)

        elif choice == "6":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice! Select 1 to 6.")
