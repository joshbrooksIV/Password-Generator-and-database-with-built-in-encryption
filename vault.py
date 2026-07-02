import json
import os
from cryptography.fernet import Fernet

print("--- My Encrypted Password Vault ---")


with open("secret.key", "rb") as key_file:
    key = key_file.read()


cipher = Fernet(key)


website = input("What website is this for?: ")
username = input("What is your username?: ")
password = input("What is the password?: ")


encrypted_password = cipher.encrypt(password.encode()).decode()


new_data = {
    website: {
        "username": username,
        "password": encrypted_password
    }
}


if os.path.exists("passwords.json"):
    with open("passwords.json", "r") as file:
        current_data = json.load(file)
    current_data.update(new_data)
else:
    current_data = new_data

with open("passwords.json", "w") as file:
    json.dump(current_data, file, indent=4)

print(f"Successfully encrypted and saved login for {website}!")
