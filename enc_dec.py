from cryptography.fernet import Fernet
import os


def generate_key():
    """Generate a key and save it to a file if not exists."""
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    """Load the previously generated key."""
    return open("secret.key", "rb").read()

def encrypt_file(input_filename="user_data", output_filename="user_data.apta"):
    """Encrypt a file and remove the original."""
    generate_key()
    key = load_key()
    cipher = Fernet(key)
    
    with open(input_filename, "rb") as file:
        file_data = file.read()
    
    encrypted_data = cipher.encrypt(file_data)
    
    with open(output_filename, "wb") as file:
        file.write(encrypted_data)
    
    os.remove(input_filename)  # Remove the original file after encryption

def decrypt_file(input_filename="user_data.apta", output_filename="user_data"):
    """Decrypt a file and remove the encrypted version."""
    key = load_key()
    cipher = Fernet(key)
    
    with open(input_filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher.decrypt(encrypted_data)
    
    with open(output_filename, "wb") as file:
        file.write(decrypted_data)
    print("decrypted")
    #os.remove(output_filename)  # Remove the encrypted file after decryption

