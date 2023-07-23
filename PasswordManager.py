from Password import Password


class PasswordManager:
    list_of_passwords: Password = []

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
