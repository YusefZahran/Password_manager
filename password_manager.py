import random
import string

from account import Account
from globals import user_accounts


class PasswordManager:
    # currently assuming there's only one user, otherwise the list of passwords will be in usermanager file

    @staticmethod
    def add_password():
        title = input("enter title name")
        username = input("enter username")
        password = input("enter password")
        details = input("input details")
        user_accounts.append(Account(title, username, password, details))

    @staticmethod
    def add_account(title, username, password, details=None):
        user_accounts.append(Account(title, username, password, details))

    @staticmethod
    def generate_password(length: int = 12) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation

        has_uppercase = False
        has_digit = False
        has_special = False

        password = ""

        while len(password) < length:
            char = random.choice(characters)
            if char in string.ascii_uppercase:
                has_uppercase = True
            elif char in string.digits:
                has_digit = True
            elif char in string.punctuation:
                has_special = True

            password += char

        if not (has_uppercase and has_digit and has_special):
            return PasswordManager.generate_password(length)

        return password

    @staticmethod
    def is_password_secure(password: str) -> bool:

        if len(password) < 8:
            return False

        has_uppercase = any(char in string.ascii_uppercase for char in password)
        has_lowercase = any(char in string.ascii_lowercase for char in password)
        has_digit = any(char in string.digits for char in password)
        has_special = any(char in string.punctuation for char in password)

        return has_uppercase and has_lowercase and has_digit and has_special
