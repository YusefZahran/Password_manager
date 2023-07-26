from FileManager import FileManager
from PasswordManager import PasswordManager
from cryptographer import Cryptographer
from ui.frames.sign_in_form import SignInForm
from ui.root_widget import RootWidget


# region Tests

def cryptographer_test():
    username = "admin"
    master_password = "P@ssw0rd"

    encrypter = Cryptographer(username, master_password)

    entry = "pass"
    token = encrypter.encrypt_entry(entry)

    decrypter = Cryptographer(username, master_password)

    decrypted = decrypter.decrypt_entry(token)

    print(decrypted)


def ui_test():
    root = RootWidget()
    root.clear_canvas()

    main_menu = SignInForm(root)
    root.add_frame(main_menu)
    root.wait_window(main_menu)
    print(f"Received: {main_menu.username_var.get()}: {main_menu.master_password_var.get()}")

    root.show()


def registration_test():
    registered_users = {}

    def register_user():
        # Get user input for username and password
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Save the username and password in the dictionary
        registered_users[username] = password

        print("Registration Successful!")
        return 0

    def login():
        # Get user input for login credentials
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the entered username and password match the dictionary entries
        if username in registered_users and registered_users[username] == password:
            print("Login Successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False

    register_user()
    # login()
    if login():
        # Place code here that executes after successful login
        print("Welcome to the system!")
    else:
        # Place code here that executes when login fails
        print("Access denied.")
    print("Test!")


def password_manager_test():
    pm = PasswordManager()
    pm.add_password()
    pm.print_passwords()

    generated_pass = pm.generate_password()
    print(generated_pass)
    print(pm.is_password_secure(generated_pass))


def file_manager_test():
    pm = PasswordManager()
    pm.add_password()

    fm = FileManager()

    fm.save_passwords()
    print(fm.load_passwords())


# endregion

# region Main
def main():
    cryptographer_test()
    ui_test()
    registration_test()

    password_manager_test()

    file_manager_test()
    return 0


if __name__ == '__main__':
    main()

# endregion
