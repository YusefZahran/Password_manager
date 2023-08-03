from file_manager import FileManager
from password_manager import PasswordManager
from cryptographer import Cryptographer
from ui.frames.accounts_list_frame import AccountsListFrame
from ui.frames.sign_in_form import SignInForm
from ui.root_widget import RootWidget
from Registeration_Login import ui_login


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


def ui_accounts_list_test():
    root = RootWidget()
    root.clear_canvas()

    main_menu = AccountsListFrame(root)
    root.add_frame(main_menu)
    root.wait_window(main_menu)

    root.show()


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


def registration_ui_test():
    if ui_login():
        # Place code here that executes after successful login
        print("Welcome to the system!")
    else:
        # Place code here that executes when login fails
        print("Access denied.")


# endregion

# region Main
def main():
    registration_ui_test()
    ui_accounts_list_test()
    ui_test()

    cryptographer_test()
    password_manager_test()
    file_manager_test()
    return 0


# endregion

# region Main
if __name__ == '__main__':
    main()
# endregion
