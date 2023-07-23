# To install library in case PyCharm couldn't: pip install tk
from cryptographer import Cryptographer
from ui.widgets.main_menu_widget import MainMenuWidget


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
    main_menu = MainMenuWidget()
    main_menu.show()


def main():
    cryptographer_test()
    ui_test()


if __name__ == '__main__':
    main()
