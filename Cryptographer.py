import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Cryptographer:
    fernet: Fernet

    def __init__(self, master_password: str):
        key = self.__generate_key(master_password)
        self.fernet = Fernet(key)

    def encrypt(self, password: str) -> bytes:
        token = self.fernet.encrypt(bytes(password, 'utf-8'))
        return token

    def decrypt(self, master_password: str, token: bytes) -> str:
        temp_key = self.__generate_key(master_password)
        temp_fernet = Fernet(temp_key)
        decryption_test = temp_fernet.decrypt(token)

        decrypted_password = self.fernet.decrypt(token)

        return decrypted_password.decode('utf-8')

    @staticmethod
    def __generate_key(master_password: str) -> bytes:
        """Generates a key using the given master password"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.urandom(32),
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(master_password, 'utf-8')))

        return key
