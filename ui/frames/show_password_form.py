import tkinter as tk
import string

from account import Account
from ui.frames.custom_frame import CustomFrame
from ui.components.custom_label import CustomLabel
from ui.components.custom_entry import CustomEntry


class ShowAccountForm(CustomFrame):
    """Show Password Form Frame"""
    # region properties
    title_var: string
    username_var: string
    password_var: string
    details_var: [string]
    title_var_entry: CustomEntry
    username_var_entry: CustomEntry
    password_var_entry: CustomEntry

    # endregion

    def __init__(self, master: tk.Misc, account: Account):
        self.title_var = account.title
        self.username_var = account.username
        self.password_var = account.get_password()
        self.title_var_entry = CustomEntry
        self.password_var_entry = CustomEntry
        self.password_var_entry = CustomEntry
        super().__init__(master)

    def initialize_frame(self):
        # Frame title
        CustomLabel(self, text="Account Information: ", x=300, y=20)

        # Title info
        CustomLabel(self, text="Title: ", x=50, y=50)
        self.title_var_entry = CustomEntry(self, x=160, y=50)
        self.title_var_entry.insert(0, self.title_var)
        self.title_var_entry.configure(state="disabled")

        # Username info
        CustomLabel(self, text="Username: ", x=50, y=80)
        self.username_var_entry = CustomEntry(self, x=160, y=80)
        self.username_var_entry.insert(0, self.username_var)
        self.username_var_entry.configure(state="disabled")

        # Password info
        CustomLabel(self, text="Password: ", x=50, y=110)
        self.password_var_entry = CustomEntry(self, x=160, y=110)
        self.password_var_entry.insert(0, self.password_var)
        self.password_var_entry.configure(state="disabled")

        edit_button = tk.Button(self, text="Edit", command=self.edit_command)
        edit_button.place(x=self.get_x_center(), y=self.get_y_center())
        exit_button = tk.Button(self, text="Exit", command=self.exit_command)
        exit_button.place(x=self.get_x_center(), y=self.get_y_center()+50)

    def edit_command(self):
        # turn the entries states om

        self.title_var_entry.configure(state="normal")
        self.username_var_entry.configure(state="normal")
        self.password_var_entry.configure(state="normal")

    def exit_command(self):
        self.destroy_frame()