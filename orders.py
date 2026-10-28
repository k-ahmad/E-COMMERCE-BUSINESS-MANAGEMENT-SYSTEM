
from datetime import datetime
from admin import products

orders = {}
next_order_id = 1001


def checkout(user, cart):
    global next_order_id

    print("\n========== CHECKOUT ==========")

    if not cart:
        print("Your cart is empty!")
        return

    # Verify stock before placing the order
    for product_id, quantity in cart.items():
        product = products.get(product_id)

        if product is None:
            print(f"Product ID {product_id} no longer exists.")
            return

        if quantity > product["quantity"]:
            print(f"Insufficient stock for {product['name']}!")
            return

    # Calculate order total
    total = 0

    for product_id, quantity in cart.items():
        product = products[product_id]
        total += product["price"] * quantity

    print(f"Order total: Rs. {total:.2f}")

    confirm = input("Confirm order? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Checkout cancelled.")
        return

    # Save a snapshot of ordered products
    order_items = []

    for product_id, quantity in cart.items():
        product = products[product_id]

        order_items.append({
            "product_id": product_id,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity,
            "subtotal": product["price"] * quantity
        })

    # Deduct stock only after successful validation
    for product_id, quantity in cart.items():
        products[product_id]["quantity"] -= quantity

    order_id = next_order_id

    orders[order_id] = {
        "order_id": order_id,
        "customer_email": user["email"],
        "customer_name": user["name"],
        "items": order_items,
        "total": total,
        "status": "Placed",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    next_order_id += 1
    cart.clear()

    print("\nOrder placed successfully!")
    print(f"Order ID: {order_id}")
    print(f"Total: Rs. {total:.2f}")
    print("Your cart has been cleared.")


def view_my_orders(user):
    print("\n========== MY ORDERS ==========")

    found = False

    for order in orders.values():
        if order["customer_email"] == user["email"]:
            found = True

            print("\n" + "-" * 35)
            print(f"Order ID: {order['order_id']}")
            print(f"Date: {order['date']}")
            print(f"Total: Rs. {order['total']:.2f}")
            print(f"Status: {order['status']}")

            for item in order["items"]:
                print(
                    f"  {item['name']} x {item['quantity']} "
                    f"= Rs. {item['subtotal']:.2f}"
                )

    if not found:
        print("You have not placed any orders yet.")


def cancel_order(user):
    print("\n========== CANCEL ORDER ==========")

    try:
        order_id = int(input("Enter your Order ID: "))
    except ValueError:
        print("Please enter a valid Order ID.")
        return

    order = orders.get(order_id)

    if order is None:
        print("Order not found!")
        return

    if order["customer_email"] != user["email"]:
        print("You cannot cancel another customer's order!")
        return

    if order["status"] != "Placed":
        print("This order cannot be cancelled.")
        return

    # Restore stock
    for item in order["items"]:
        product_id = item["product_id"]

        if product_id in products:
            products[product_id]["quantity"] += item["quantity"]

    order["status"] = "Cancelled"

    print(f"Order {order_id} cancelled successfully!")
    print("Product stock has been restored.")
