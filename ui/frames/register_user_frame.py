import tkinter as tk

import globals
from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame
from ui.frames.sign_in_frame import SignInFrame


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
        CustomVerticalInputField(self, "Master Password", self.__registered_password, show='*',
                                 x=self.get_x_center(), y=self.get_y_center() - 25)

        CustomVerticalInputField(self, "Confirm Password", self.__registered_confirmed_password, show='*',
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

        if username == "" or password == "" or confirmed_password == "":
            if self.__error_label is not None:
                self.__error_label.destroy()
            self.__error_label = tk.Label(self, text="Please fill in all the fields", fg="red")
            self.__error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return

        if password != confirmed_password:
            if self.__error_label is not None:
                self.__error_label.destroy()
            self.__error_label = tk.Label(self, text="confirm password does not match", fg="red")
            self.__error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return

        # TODO: Fix this issue
        self.__register_user(username, password)
        self.pack_forget()
        SignInFrame(self.master).show()
        self.destroy_frame()
        self.pack_forget()

    # endregion

    @staticmethod
    def __register_user(username, password):
        """Registers a new user by adding a new user to the registered users dictionary"""
        # Get user input for username and password
        new_username = username
        new_password = password

        # Save the username and password in the dictionary
        globals.registered_users[new_username] = new_password