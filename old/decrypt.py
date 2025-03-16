from cryptography.fernet import Fernet
import os

def load_key():
    """Load the encryption key from a file."""
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

def decrypt_file(encrypted_file_path):
    """Decrypt the given encrypted file using the encryption key."""
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    original_file_path = encrypted_file_path.replace(".apta", "")
    with open(original_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    os.remove("user_data")

