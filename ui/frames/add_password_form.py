import tkinter as tk
import string

from password_manager import PasswordManager
from ui.frames.custom_frame import CustomFrame
from ui.components.custom_label import CustomLabel
from ui.components.custom_entry import CustomEntry


class AddAccountFrame(CustomFrame):
    title_var: string
    username_var: string
    password_var: string
    details_var: [string]
    title_var_entry: tk.StringVar
    username_var_entry: tk.StringVar
    password_var_entry: tk.StringVar

    def __init__(self, master: tk.Misc):
        self.title_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.details_var = tk.StringVar()
        super().__init__(master)

    def initialize_frame(self):
        # Form Title
        CustomLabel(self, text="Enter Account Information", x=self.get_x_center(),
                    y=self.get_y_center() - 200)

        # Title info
        CustomLabel(self, text="Title: ", x=50, y=50)
        CustomEntry(self, text_variable=self.title_var, x=160, y=50)

        # Username info
        CustomLabel(self, text="Username: ", x=50, y=80)
        CustomEntry(self, text_variable=self.username_var, x=160, y=80)

        # Password info
        CustomLabel(self, text="Password: ", x=50, y=110)
        CustomEntry(self, text_variable=self.password_var, x=160, y=110)

        add_button = tk.Button(self, text="Add", command=self.add_password)
        add_button.place(x=self.get_x_center(), y=self.get_y_center())

    def add_password(self):
        PasswordManager.add_password(self.title_var, self.username_var, self.password_var, self.details_var)
        self.destroy_frame()
