import hashlib
import json
import os
import tkinter as tk

from cryptographer import Cryptographer
import globals
from password_manager import PasswordManager
from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame


class RegisterUserFrame(CustomFrame):
    """Register user frame. Used to allow users to register"""
    # region Properties
    __registered_username: tk.StringVar
    """The username tkinter variable"""
    __registered_password: tk.StringVar
    """The password tkinter variable"""
    __registered_confirmed_password: tk.StringVar
    """The confirmed password tkinter variable"""

    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        """Register User Frame constructor
        :param master: The master component
        """
        self.__registered_username = tk.StringVar()
        self.__registered_password = tk.StringVar()
        self.__registered_confirmed_password = tk.StringVar()
        self.__error_label = None

        super().__init__(master)

    # endregion

    # region UI
    def initialize_frame(self):
        """Initializes the frame by drawing UI components"""
        # Username
        CustomVerticalInputField(self, "Username", self.__registered_username,
                                 x=self.get_x_center(), y=self.get_y_center() - 100)

        # Username
        CustomVerticalInputField(self, "Master Password", self.__registered_password, show='ඞ',
                                 x=self.get_x_center(), y=self.get_y_center() - 25)

        CustomVerticalInputField(self, "Confirm Password", self.__registered_confirmed_password, show='ඞ',
                                 x=self.get_x_center(), y=self.get_y_center() + 50)

        # Submit
        submit_button = tk.Button(self, text="Sign Up", command=self.__submit_command)
        submit_button.place(x=self.get_x_center(), y=self.get_y_center() + 125, anchor=tk.CENTER)

    # endregion

    # region Commands
    def __submit_command(self):
        """Submits the given information and adds a new user to the users list"""
        username = self.__registered_username.get()
        password = self.__registered_password.get()
        confirmed_password = self.__registered_confirmed_password.get()

        if not self.__is_valid_username_and_password(username, password, confirmed_password):
            return

        self.__register_user(username, password)
        self.destroy_frame()

    # endregion
    def __is_valid_username_and_password(self, username: str, password: str, confirmed_password: str) -> bool:
        """Checks if the given username and password and confirmed password are valid"""
        if self.__fields_are_empty(username, password, confirmed_password):
            return False

        if self.__username_is_taken(username):
            return False

        if not self.__password_is_equal_confirm_password(password, confirmed_password):
            return False

        if not self.__password_is_secure(password):
            return False

        return True

    def __username_is_taken(self, username: str) -> bool:
        """Checks if the given username is not taken"""
        if username in globals.registered_users:
            if self.__error_label is not None:
                self.__error_label.destroy()
            self.__error_label = tk.Label(self, text="Username already exists", fg="red")
            self.__error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return True
        return False

    def __password_is_secure(self, password: str) -> bool:
        """Checks if the given password is secure enough"""
        if not PasswordManager.is_password_secure(password):
            if self.__error_label is not None:
                self.__error_label.destroy()
            self.__error_label = tk.Label(self, text="Password is not safe enough", fg="red")
            self.__error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return False
        return True

    def __fields_are_empty(self, username: str, password: str, confirmed_password: str) -> bool:
        """Checks if the given username and password and confirmed password are not empty"""
        if username == "" or password == "" or confirmed_password == "":
            if self.__error_label is not None:
                self.__error_label.destroy()
            self.__error_label = tk.Label(self, text="Please fill in all the fields", fg="red")
            self.__error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return True
        return False

    def __password_is_equal_confirm_password(self, password: str, confirmed_password: str) -> bool:
        """Checks if the given password is equal to the confirmed password"""
        if password != confirmed_password:
            if self.__error_label is not None:
                self.__error_label.destroy()
            self.__error_label = tk.Label(self, text="Password does not match confirm password", fg="red")
            self.__error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return False
        return True

    @staticmethod
    def __register_user(username, password):
        """Registers a new user by adding a new user to the registered users dictionary"""

        # Save the username and password in the dictionary
        globals.registered_users[username] = password

        encrypter = Cryptographer(username, password)
        password_token = encrypter.encrypt_entry(password)

        file_name = Cryptographer.hash_entry(username)
        file_path = f"{globals.USERS_DIRECTORY}/{file_name}.json"

        with open(file_path, "w") as f:
            json.dump(password_token.decode('utf-8'), f)

        os.makedirs(f"{globals.ACCOUNTS_DIRECTORY}/{file_name}/")
