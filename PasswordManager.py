import random
import string

from Password import Password


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
        letter_list: string = ["uppercase", "lowercase", "punc", "nums"]
        chars_changed = False * length
        pw: string = ""
        for i in range(length):
            c = random.choice(list(string.ascii_lowercase))
            pw += c
        nog = length/2
        it = nog
        while(nog >0):
            idx = random.randint(0, length - 1)
            if not chars_changed[idx]:
                nog -= 1
                choice = random.choice(letter_list)
                if choice == "uppercase":
                    c = random.choice(list(string.ascii_uppercase))
                elif choice == "lowercase":
                    c = random.choice(list(string.ascii_lowercase))
                elif choice == "punc":
                    c = random.choice(list(string.punctuation))
                else:
                    c = random.choice(list(string.digits))
                pw[idx] = c
        # for i in range(length):
        #     if i == 0 or i == 1 or i == length-1:
        #         c = random.choice(list(string.ascii_lowercase))
        #     else:
        #         choice = random.choice(letter_list)
        #         if choice == "uppercase":
        #             c = random.choice(list(string.ascii_uppercase))
        #         elif choice == "lowercase":
        #             c = random.choice(list(string.ascii_lowercase))
        #         elif choice == "punc":
        #             c = random.choice(list(string.punctuation))
        #         else:
        #             c = random.choice(list(string.digits))
        #     pw += c
        return pw

    @staticmethod
    def is_password_secure(password: str) -> bool:
        if len(password) < 12:
            return False

        has_uppercase = any(char in string.ascii_uppercase for char in password)
        has_lowercase = any(char in string.ascii_lowercase for char in password)
        has_digit = any(char in string.digits for char in password)
        has_special = any(char in string.punctuation for char in password)

        return has_uppercase and has_lowercase and has_digit and has_special
