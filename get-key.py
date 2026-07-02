import json
import os
from cryptography.fernet import Fernet

print("--- Password Vault Retriever ---")

# 1. Load the secret key to unlock the data
if not os.path.exists("secret.key"):
    print("Error: secret.key file missing!")
    exit()

with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# 2. Check if the vault file exists
if not os.path.exists("passwords.json"):
    print("Error: No passwords saved yet!")
    exit()

# 3. Load the database
with open("passwords.json", "r") as file:
    current_data = json.load(file)

# 4. Ask the user which site they want to look up
search_site = input("Which website do you need the password for?: ")

# 5. Look it up and decrypt it!
if search_site in current_data:
    username = current_data[search_site]["username"]
    encrypted_password = current_data[search_site]["password"]
    
    # UN-SCRAMBLE IT!
    decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
    
    print("\n--- Credentials Found ---")
    print(f"Username: {username}")
    print(f"Password: {decrypted_password}")
else:
    print(f"No entry found for {search_site}.")
