import FileManager
from PasswordManager import PasswordManager


# region Main
def main():
    """ Main program """
    register_user()
    # login()
    if login():
        # Place code here that executes after successful login
        print("Welcome to the system!")
    else:
        # Place code here that executes when login fails
        print("Access denied.")
    print("Test!")
    pm = PasswordManager()
    pm.add_password()
    pm.print_passwords()

    file_manager_test()
    # fuck yea
    return 0


if __name__ == "__main__":
    main()

# endregion

# region Registration
# Dictionary to store registered users' credentials
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


# endregion

# region Tests

def file_manager_test():
    pm = PasswordManager()
    pm.add_password()

    fm = FileManager()

    fm.save_passwords()
    print(fm.load_passwords())

# endregion
