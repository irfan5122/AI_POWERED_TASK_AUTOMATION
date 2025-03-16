from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

print("Encryption key saved!")

with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Encrypt the file
with open("user_data", "rb") as file:
    file_data = file.read()

encrypted_data = fernet.encrypt(file_data)

with open("user_data.apta", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

os.remove("user_data")