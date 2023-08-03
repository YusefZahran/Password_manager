import tkinter as tk
from Password import Account
import string

# from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame
from ui.components.custom_label import CustomLabel


class ShowPasswordForm(CustomFrame):
    """Show Password Form Frame"""
    # region properties
    title_var: string
    username_var: string
    password_var: string
    details_var: string
    # endregion

    def __init__(self, master: tk.Misc, account: Account):
        super().__init__(master)
        title_var = account.title
        username_var = account.username
        password_var = account.get_password()
        # details = account.details



    def initialize_frame(self):
        t_label = CustomLabel(self, text="title", x=50, y=50)