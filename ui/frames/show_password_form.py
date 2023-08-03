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

    def __init__(self, master: tk.Misc,account: Account):
        title_var = account.title
        username_var = account.username
        password_var = account.get_password()
        # details = account.details
        t_label = CustomLabel(self, master, text=title_var, x=50, y=50)
        super.__init__(super, master)
