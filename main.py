import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.key = self.generate_key()

    def generate_key(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.urandom(32),
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(self.master_password, 'utf-8')))
        return key

    def encrypt_entry(self, entry):
        cipher = Fernet(self.key)
        encrypted_entry = cipher.encrypt(entry.encode())
        # Store the encrypted_entry securely (e.g., in a file or database)
        return encrypted_entry

    def decrypt_entry(self, encrypted_entry):
        cipher = Fernet(self.key)
        decrypted_entry = cipher.decrypt(encrypted_entry)
        return decrypted_entry.decode()


# Example usage:
master_password = input("Enter your master password: ")
password_manager = PasswordManager(master_password)

pm2 = PasswordManager(master_password)

print(password_manager.key)
print(pm2.key)

c1 = Fernet(password_manager.key)
token = c1.encrypt(b"Password")

c2 = Fernet(password_manager.key)
print(c2.decrypt(token))

c3 = Fernet(pm2.key)
print(c3.decrypt(token))
