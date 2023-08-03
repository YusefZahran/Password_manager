import tkinter as tk
from Password import Account
import string

# from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame
from ui.components.custom_label import CustomLabel
from ui.components.custom_entry import CustomEntry


class ShowPasswordForm(CustomFrame):
    """Show Password Form Frame"""
    # region properties
    title_var: string
    username_var: string
    password_var: string
    details_var: string
    # endregion

    def __init__(self, master: tk.Misc, account: Account):
        self.title_var = account.title
        self.username_var = account.username
        self.password_var = account.get_password()
        super().__init__(master)

        # details = account.details

    def initialize_frame(self):
        # Frame title
        form_title = CustomLabel(self, text="Account Information: ", x=300,y=20)

        # Title info
        title_label = CustomLabel(self, text="Title: ", x=50, y=50 )
        title_var_entry = CustomEntry(self, x=160, y=50 )
        title_var_entry.insert(0, self.title_var)
        title_var_entry.configure(state="disabled")

        # Username info
        username_label = CustomLabel(self, text="Username: ", x=50, y=80)
        username_var_entry = CustomEntry(self, x=160,y= 80)
        username_var_entry.insert(0, self.username_var)
        username_var_entry.configure(state="disabled", background="black")

        # Password infp
        password_label = CustomLabel(self, text="Password: ", x=50, y=110)
        password_var_entry = CustomEntry(self, x= 160, y=110)
        password_var_entry.insert(0, self.password_var)
        password_var_entry.configure(state="disabled")

        # username_label .config( anchor="w", justify="left" )
        # username_var_label = CustomLabel(self, text=self.username_var, x=80, y=80)
        # username_var_label.config( anchor="w", justify="left")
