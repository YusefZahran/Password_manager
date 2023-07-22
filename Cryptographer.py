import base64
import hashlib
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from globals import SALT_DIRECTORY


class Cryptographer:
    """Cryptographer class. Responsible for generating keys, encrypting, and decrypting"""
    __username: str
    """The user username used for salt"""
    __master_password: str
    """The user master password used for key generation and salt"""
    __salt: bytes
    """The salt generated from the username and the master password"""
    __key: bytes
    """The key used for symmetric encryption"""

    def __init__(self, username: str, master_password: str):
        self.__username = username
        self.__master_password = master_password

        self.__initialize_dirs()
        self.__generate_salt()
        self.__generate_key()

    @staticmethod
    def __initialize_dirs():
        if not os.path.exists(SALT_DIRECTORY):
            os.makedirs(SALT_DIRECTORY)

    def __generate_salt(self):
        file_name = self.__username + self.__master_password
        salt_hash = hashlib.md5(file_name.encode('utf-8'))
        salt_path = SALT_DIRECTORY + str(salt_hash.hexdigest())

        if not os.path.exists(salt_path):
            self.__salt = os.urandom(32)
            f = open(salt_path, "w")
            f.write(str(self.__salt))
            f.close()
        else:
            f = open(salt_path, "r")
            str_salt = f.readline()
            f.close()

            str_salt = str_salt.replace('b', '', 1)
            str_salt = str_salt.replace("'", '')
            self.__salt = bytes(str_salt, 'utf-8')

    def __generate_key(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.__salt,
            iterations=100000,
            backend=default_backend()
        )

        self.__key = base64.urlsafe_b64encode(kdf.derive(bytes(self.__master_password, 'utf-8')))

    def encrypt_entry(self, entry):
        cipher = Fernet(self.__key)
        encrypted_entry = cipher.encrypt(entry.encode())
        return encrypted_entry

    def decrypt_entry(self, encrypted_entry):
        cipher = Fernet(self.__key)
        decrypted_entry = cipher.decrypt(encrypted_entry)
        return decrypted_entry.decode()
