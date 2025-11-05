from cryptography.fernet import Fernet
import os

# Uncomment and run once to create key.key file if you don't have one:
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Generate key if missing
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

key = load_key()
fer = Fernet(key)

def view():
    if not os.path.exists("Passwords.txt"):
        print("No passwords stored yet.")
        return
    with open("Passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Account:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("Passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view), press q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode selected.")
        continue