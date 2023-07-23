# To install library in case PyCharm couldn't: pip install tk
import tkinter

from cryptographer import Cryptographer
from ui.frames.main_menu_frame import MainMenuFrame
from ui.root_widget import RootWidget


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

    main_menu = MainMenuFrame(root)
    root.add_frame(main_menu)
    root.wait_window(main_menu)

    root.show()


def main():
    cryptographer_test()
    ui_test()


if __name__ == '__main__':
    main()
