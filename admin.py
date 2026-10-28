
products = {}
next_product_id = 1


def add_product():
    global next_product_id

    print("\n--- Add New Product ---")

    name = input("Enter product name: ").strip()
    if not name:
        print("Product name cannot be empty!")
        return

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter stock quantity: "))

        if price <= 0 or quantity < 0:
            print("Price must be positive and quantity cannot be negative!")
            return

    except ValueError:
        print("Please enter a valid price and quantity!")
        return

    products[next_product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    print(f"Product added successfully! ID: {next_product_id}")
    next_product_id += 1


def view_products():
    print("\n--- All Products ---")

    if not products:
        print("No products available.")
        return

    for product_id, product in products.items():
        print(f"\nProduct ID: {product_id}")
        print(f"Name: {product['name']}")
        print(f"Price: Rs. {product['price']:.2f}")
        print(f"Stock: {product['quantity']}")


def search_product():
    print("\n--- Search Product ---")

    search_name = input("Enter product name: ").strip().lower()
    found = False

    for product_id, product in products.items():
        if search_name in product["name"].lower():
            print(f"\nID: {product_id}")
            print(f"Name: {product['name']}")
            print(f"Price: Rs. {product['price']:.2f}")
            print(f"Stock: {product['quantity']}")
            found = True

    if not found:
        print("Product not found!")


def update_product():
    print("\n--- Update Product ---")

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Product ID must be a number!")
        return

    if product_id not in products:
        print("Product not found!")
        return

    product = products[product_id]

    print("1. Update Name")
    print("2. Update Price")
    print("3. Update Stock")

    choice = input("Choose what to update: ")

    if choice == "1":
        name = input("Enter new name: ").strip()

        if name:
            product["name"] = name
            print("Product name updated!")
        else:
            print("Name cannot be empty!")

    elif choice == "2":
        try:
            price = float(input("Enter new price: "))

            if price <= 0:
                print("Price must be greater than zero!")
                return

            product["price"] = price
            print("Product price updated!")

        except ValueError:
            print("Invalid price!")

    elif choice == "3":
        try:
            quantity = int(input("Enter new stock quantity: "))

            if quantity < 0:
                print("Stock cannot be negative!")
                return

            product["quantity"] = quantity
            print("Stock updated!")

        except ValueError:
            print("Invalid quantity!")

    else:
        print("Invalid choice!")


def delete_product():
    print("\n--- Delete Product ---")

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Product ID must be a number!")
        return

    if product_id in products:
        deleted_product = products.pop(product_id)
        print(f"{deleted_product['name']} deleted successfully!")
    else:
        print("Product not found!")


def admin_panel():
    while True:
        print("\n========== ADMIN PANEL ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            break

        else:
            print("Invalid choice! Select 1 to 6.")
