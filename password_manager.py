import random
import string

from password import Password


class PasswordManager:
    list_of_passwords: [Password] = []

    # currently assuming there's only one user, otherwise the list of passwords will be in a usermanager file

    def add_password(self):
        title = input("enter title name")
        username = input("enter username")
        password = input("enter password")
        details = input("input details")
        self.list_of_passwords.append(Password(title, username, password, details))

    def print_passwords(self):
        for password in self.list_of_passwords:
            print(password.__str__())

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
        if len(password) < 12:
            return False

        has_uppercase = any(char in string.ascii_uppercase for char in password)
        has_lowercase = any(char in string.ascii_lowercase for char in password)
        has_digit = any(char in string.digits for char in password)
        has_special = any(char in string.punctuation for char in password)

        return has_uppercase and has_lowercase and has_digit and has_special
