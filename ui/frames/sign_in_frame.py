import hashlib
import json
import os
import tkinter as tk

from cryptographer import Cryptographer
import globals
from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame


class SignInFrame(CustomFrame):
    # region Properties
    username_var: tk.StringVar
    master_password_var: tk.StringVar
    is_logged_in: bool

    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        self.username_var = tk.StringVar()
        self.master_password_var = tk.StringVar()
        self.error_label = None
        self.is_logged_in = False
        self.is_register = False
        super().__init__(master)

    # endregion
    def switch_to_register(self):
        self.is_register = True
        self.pack_forget()
        self.destroy_frame()

    # region UI
    def initialize_frame(self):

        # Username
        CustomVerticalInputField(self, "Username", self.username_var,
                                 x=self.get_x_center(), y=self.get_y_center() - 100)

        # Username
        CustomVerticalInputField(self, "Master Password", self.master_password_var, show='ඞ',
                                 x=self.get_x_center(), y=self.get_y_center() - 25)

        # region Submit
        submit_button = tk.Button(self, text="Don't have an account ?", command=self.switch_to_register)
        submit_button.place(x=self.get_x_center() + 220, y=self.get_y_center() - 180, anchor=tk.CENTER)

        submit_button = tk.Button(self, text="Sign in", command=self.submit_command)
        submit_button.place(x=self.get_x_center(), y=self.get_y_center() + 70, anchor=tk.CENTER)

        # endregion

    # endregion

    # region Commands
    def submit_command(self):
        str_error = "Please fill in all the fields"
        lbl2 = "Username or password may be wrong "

        if self.username_var.get() == "" or self.master_password_var.get() == "":
            if self.error_label is not None:
                self.error_label.destroy()
            self.error_label = tk.Label(self, text=str_error, fg="red")
            self.error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return

        username = self.username_var.get()
        password = self.master_password_var.get()
        self.show()

        if self.login(username, password):
            return True
        else:
            # Place code here that executes when login fails
            if self.error_label is not None:
                self.error_label.destroy()
            self.error_label = tk.Label(self, text=lbl2, fg="red")
            self.error_label.place(x=self.get_x_center(), y=self.get_y_center() + 125, anchor=tk.CENTER)

        # self.destroy_frame()
        return False

    # endregion

    def login(self, username, password):
        is_logged_in = False
        # TODO: Create class for this
        file_name = hashlib.sha256()
        file_name.update(bytes(username, 'utf-8'))
        file_name = file_name.hexdigest()
        file_path = f"{globals.USERS_DIRECTORY}/{file_name}.json"
        if os.path.exists(file_path):
            globals.cryptographer = Cryptographer(username, password)
            with open(file_path, "r") as infile:
                data = json.load(infile)
                decrypted_password = globals.cryptographer.decrypt_entry(data)
                if password == decrypted_password:
                    is_logged_in = True

        if is_logged_in:
            globals.CURRENT_USER_ACCOUNTS_DIR = f"{globals.ACCOUNTS_DIRECTORY}/{file_name}/"
            self.is_logged_in = True
            self.destroy_frame()
            return True
        else:
            self.is_logged_in = False
            return False
