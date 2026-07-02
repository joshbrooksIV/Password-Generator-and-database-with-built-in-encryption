# Encrypted Password Vault

A secure Python-based password manager built inside a Linux (Crostini) environment. This project generates random secure passwords, links them to specific websites/usernames, and encrypts the data before saving it to a local database.

## Features
- **Random Generation:** Generates highly secure, randomized passwords.
- **Local Database:** Stores website credentials neatly using JSON files.
- **Fernet Encryption:** Uses AES-based encryption from the `cryptography` library to scramble passwords so they are safe from plain-text exposure.

## How to Run
1. Install dependencies: `pip install cryptography`
2. Run `make_key.py` once to generate your unique `secret.key`.
3. Use `vault.py` to add new credentials.
4. Use `get_password.py` to decrypt and retrieve your passwords.
