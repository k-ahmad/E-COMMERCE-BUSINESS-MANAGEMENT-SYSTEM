
import json
import os
import hashlib

DATA_FOLDER = "data"
USERS_FILE = os.path.join(DATA_FOLDER, "users.json")


def load_users():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as file:
            json.dump({}, file)

    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_users(users):
    os.makedirs(DATA_FOLDER, exist_ok=True)

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user():
    print("\n========== CUSTOMER REGISTRATION ==========")

    users = load_users()

    name = input("Enter your full name: ").strip()
    email = input("Enter your email: ").strip().lower()
    password = input("Create password: ")
    confirm_password = input("Confirm password: ")

    if not name or not email or not password:
        print("All fields are required!")
        return

    if "@" not in email or "." not in email:
        print("Please enter a valid email!")
        return

    if email in users:
        print("This email is already registered!")
        return

    if len(password) < 8:
        print("Password must contain at least 8 characters!")
        return

    if password != confirm_password:
        print("Passwords do not match!")
        return

    users[email] = {
        "name": name,
        "password": hash_password(password),
        "role": "customer"
    }

    save_users(users)

    print(f"\nWelcome, {name}!")
    print("Your account has been created successfully.")


def login_user():
    print("\n========== LOGIN ==========")

    users = load_users()

    email = input("Enter your email: ").strip().lower()
    password = input("Enter your password: ")

    if email not in users:
        print("Account not found. Please register first.")
        return None

    if users[email]["password"] != hash_password(password):
        print("Incorrect password!")
        return None

    print(f"\nLogin successful! Welcome {users[email]['name']}.")

    return {
        "email": email,
        "name": users[email]["name"],
        "role": users[email]["role"]
    }
