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
    details_var_entry: CustomEntry
    edit_button: tk.Button
    exit_button: tk.Button
    is_edit: bool

    # endregion

    def __init__(self, master: tk.Misc, account: Account):
        # initializing account values
        self.title_var = account.title
        self.username_var = account.username
        self.password_var = account.get_password()
        details_string = ""
        for detail in account.details:
            details_string = details_string + detail + ", "  # seperating the details
        self.details_var = details_string

        # initializing entries
        self.title_var_entry = CustomEntry
        self.password_var_entry = CustomEntry
        self.password_var_entry = CustomEntry
        self.details_var_entry = CustomEntry

        # initializing buttons
        self.edit_button = tk.Button
        self.exit_button = tk.Button

        self.is_edit = False

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

        # Details info
        CustomLabel(self, text="Details: ", x=50, y=140)
        self.details_var_entry = CustomEntry(self, x=160, y=140)
        self.details_var_entry.insert(0, self.details_var)
        self.details_var_entry.configure(state="disabled")

        # Edit button
        self.edit_button = tk.Button(self, text="Edit", command=self.edit_command)
        self.edit_button.place(x=self.get_x_center(), y=self.get_y_center())

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_command)
        self.exit_button.place(x=self.get_x_center(), y=self.get_y_center() + 50)

    def edit_command(self):
        # turn the entries states om
        if not self.is_edit:
            self.title_var_entry.configure(state="normal")
            self.username_var_entry.configure(state="normal")
            self.password_var_entry.configure(state="normal")
            self.details_var_entry.configure(state="normal")
            self.edit_button.configure(text="Show")
            self.is_edit = True
        else:
            self.title_var_entry.configure(state="disabled")
            self.username_var_entry.configure(state="disabled")
            self.password_var_entry.configure(state="disabled")
            self.details_var_entry.configure(state="disabled")
            self.edit_button.configure(text="Edit")
            self.is_edit = False

    def exit_command(self):
        self.destroy_frame()
