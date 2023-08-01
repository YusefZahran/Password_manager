# To install library in case PyCharm couldn't: pip install tk
import tkinter
from FileManager import FileManager
from PasswordManager import PasswordManager
from cryptographer import Cryptographer
from ui.frames.main_menu_frame import MainMenuFrame
from ui.frames.Register_User_frame import RegisterUserFrame
from ui.root_widget import RootWidget
from Registeration_Login import *



# endregion

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



def file_manager_test():
    pm = PasswordManager()
    pm.add_password()

    fm = FileManager()

    fm.save_passwords()
    print(fm.load_passwords())


# endregion

# region Main
def main():
    #cryptographer_test()
    #ui_test_register()
    """ Main program """
    # login()
    if ui_login():
        # Place code here that executes after successful login
        print("Welcome to the system!")
    else:
        # Place code here that executes when login fails
        print("Access denied.")

    # print("Test!")
    # pm = PasswordManager()
    # pm.add_password()
    # pm.print_passwords()

    # file_manager_test()
    # fuck yea
    return 0


if __name__ == '__main__':
    main()

# endregion
