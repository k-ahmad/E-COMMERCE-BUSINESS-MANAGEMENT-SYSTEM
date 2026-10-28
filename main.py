# Import files

from admin import admin_panel
from auth import register_user, login_user
from customer import customer_panel
from orders import view_my_orders, cancel_order


# Main menu
def main_menu():
    print(" \n E-COMMERCE BUSINESS MANAGEMENT SYSTEM")

    print("1. Admin Panel")
    print("2. Customer Panel")
    print("3. Register New Account")
    print("4. Login")
    print("5. View My Orders")
    print("6. Cancel Order")
    print("7. Exit")

# Main program
while True:
    main_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        admin_panel()

    elif choice == "2":
        user = login_user()

        if user is not None:
            if user["role"] == "customer":
                customer_panel(user)
            else:
                print("Please use the Admin Panel for admin features.")

    elif choice == "3":
        register_user()

    elif choice == "4":
        user = login_user()

        if user is not None:
            if user["role"] == "customer":
                print("Login successful!")
                customer_panel(user)
            else:
                print("Admin dashboard is not connected yet.")

    elif choice == "5":
        user = login_user()

        if user is not None and user["role"] == "customer":
            view_my_orders(user)

    elif choice == "6":
        user = login_user()

        if user is not None and user["role"] == "customer":
            cancel_order(user)

    elif choice == "7":
        print("\nThank you for using our system!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 to 7.")
