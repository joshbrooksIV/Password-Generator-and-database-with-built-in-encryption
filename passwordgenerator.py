import random
password = ""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ1234567890-=[]'#;,./<>?:@~{}+_¬!£$%^&*()"
passwordlength = int(input("How long does the password have to be? "))

for i in range(passwordlength):
    password += random.choice(chars)

print(f"Your secure password has been generated as {password}.")
