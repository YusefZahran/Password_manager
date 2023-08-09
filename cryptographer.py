import base64
import hashlib
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from globals import SALT_DIRECTORY


class Cryptographer:
    """Cryptographer class. Responsible for generating keys, encrypting, and decrypting."""

    def __init__(self, username: str, master_password: str):
        """
        Initializes a cryptographer with its salt, key, and files.

        :param username: The username used within the cryptographer for generation.
        :param master_password: The master password used within the cryptographer for generation.
        """
        self.__username = username
        self.__master_password = master_password

        self.__initialize_dirs()
        self.__generate_salt()
        self.__generate_key()

    @staticmethod
    def __initialize_dirs():
        """Initializes any directories needed for salt storage."""
        if not os.path.exists(SALT_DIRECTORY):
            os.makedirs(SALT_DIRECTORY)

    def __generate_salt(self):
        """Generates a new salt for the user if no previous salts exist for them. Otherwise, retrieves the user's
        salt."""
        file_name = self.__username + self.__master_password
        salt_hash = hashlib.md5(file_name.encode('utf-8'))
        salt_path = SALT_DIRECTORY + str(salt_hash.hexdigest())

        # If this stops working check the snapshot previous to the one titled "Drastic Code Refactoring"
        if not os.path.exists(salt_path):
            self.__salt = os.urandom(32)
            with open(salt_path, "wb") as f:
                f.write(self.__salt)
        else:
            with open(salt_path, "rb") as f:
                self.__salt = f.read()

    def __generate_key(self):
        """Generates a key for symmetric encryption."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.__salt,
            iterations=100000,
            backend=default_backend()
        )

        self.__key = base64.urlsafe_b64encode(kdf.derive(bytes(self.__master_password, 'utf-8')))

    def encrypt_entry(self, entry):
        """
        Encrypts the given entry and returns a token.
        :param entry: The given entry to encrypt.
        :return: The encrypted token.
        """
        cipher = Fernet(self.__key)
        encrypted_entry = cipher.encrypt(entry.encode())
        return encrypted_entry

    def decrypt_entry(self, token):
        """
        Decrypts the given token.
        :param token: The token to decrypt.
        :return: The decrypted token.
        """
        cipher = Fernet(self.__key)
        decrypted_entry = cipher.decrypt(token)
        return decrypted_entry.decode()

    def generate_data_from_entries(self, *args):
        data = ""
        for arg in args:
            data += self.encrypt_entry(arg).decode('utf-8') + "\n"
        return data
