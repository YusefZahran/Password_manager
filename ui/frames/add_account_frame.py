import tkinter as tk
from password_manager import PasswordManager
from ui.frames.custom_frame import CustomFrame
from ui.components.custom_label import CustomLabel
from ui.components.custom_entry import CustomEntry


class AddAccountFrame(CustomFrame):
    """Add account frame. Used to add a new account entry"""

    def __init__(self, master: tk.Misc):
        """
        Add account form constructor.

        :param master: The master component.
        """
        self.__title_var = tk.StringVar()
        self.__username_var = tk.StringVar()
        self.__password_var = tk.StringVar()
        self.__details_var = tk.StringVar()
        self.__details_var_entry = None

        super().__init__(master)

    def initialize_frame(self):
        """Initializes the frame by drawing UI components"""
        # Form Title
        CustomLabel(self, text="Enter Account Information", x=self.get_x_center(), y=self.get_y_center() - 200)

        # Title info
        CustomLabel(self, text="Title: ", x=50, y=50)
        CustomEntry(self, text_variable=self.__title_var, x=160, y=50)

        # Username info
        CustomLabel(self, text="Username: ", x=50, y=80)
        CustomEntry(self, text_variable=self.__username_var, x=160, y=80)

        # Password info
        CustomLabel(self, text="Password: ", x=50, y=110)
        CustomEntry(self, text_variable=self.__password_var, show='ඞ', x=160, y=110)

        # Details info
        CustomLabel(self, text="Details: ", x=50, y=140)
        self.__details_var_entry = CustomEntry(self, x=160, y=140)

        add_button = tk.Button(self, text="Add", command=self.__add_account_command)
        add_button.place(x=self.get_x_center(), y=self.get_y_center())

    def __add_account_command(self):
        """Adds a new account entry to the user accounts"""
        self.__details_var = self.__details_var_entry.get().strip().split(", ")
        PasswordManager.add_account(self.__title_var.get(), self.__username_var.get(),
                                    self.__password_var.get(), self.__details_var)
        self.destroy_frame()
