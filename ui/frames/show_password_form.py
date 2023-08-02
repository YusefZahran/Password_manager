import tkinter as tk
from Password import Account

# from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame


class ShowPasswordForm(CustomFrame):
    """Show Password Form Frame"""
    # region properties
    title_var: tk.StringVar
    username_var: tk.StringVar
    password_var: tk.StringVar
    details_var: tk.StringVar
    # endregion

def __init__(self, master: tk.Misc,account: Account):
    title_var = account.title
    username_var = account.username
    password_var = account.get_password()
    #details = 