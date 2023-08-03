import tkinter as tk

from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame
from ui.frames.main_menu_frame import MainMenuFrame


class RegisterUserFrame(CustomFrame):
    # region Properties
    registered_username: tk.StringVar
    registered_password: tk.StringVar
    registered_confirmed_password: tk.StringVar

    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        self.registered_username = tk.StringVar()
        self.registered_password = tk.StringVar()
        self.registered_confirmed_password = tk.StringVar()
        self.error_label = None

        super().__init__(master)

    # endregion

    # region UI
    def initialize_frame(self):
        # Username
        CustomVerticalInputField(self, "Username", self.registered_username,
                                 x=self.get_x_center(), y=self.get_y_center()-100)

        # Username
        CustomVerticalInputField(self, "Master Password", self.registered_password, show='*',
                                 x=self.get_x_center(), y=self.get_y_center()-25)

        CustomVerticalInputField(self, "Confirm Password", self.registered_confirmed_password, show='*',
                                 x=self.get_x_center(), y=self.get_y_center()+50)

        # region Submit
        submit_button = tk.Button(self, text="Sign Up", command=self.submit_command)
        submit_button.place(x=self.get_x_center(), y=self.get_y_center() + 125, anchor=tk.CENTER)
        # endregion

    # endregion

    # region Commands
    def submit_command(self):
        print(f"Submitted: {self.registered_username.get()}: {self.registered_password.get()}")
        username = self.registered_username.get()
        password = self.registered_password.get()
        confirmed_password = self.registered_confirmed_password.get()

        if username == "" or password == "" or confirmed_password == "":
            if self.error_label is not None:
                self.error_label.destroy()
            self.error_label = tk.Label(self, text="Please fill in all the fields", fg="red")
            self.error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return

        if password != confirmed_password:
            if self.error_label is not None:
                self.error_label.destroy()
            self.error_label = tk.Label(self, text="confirm password does not match", fg="red")
            self.error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return

        # TODO: Fix circular dependancies
        # register_user(username, password)
        self.pack_forget()
        MainMenuFrame(self.master).show()
        self.destroy_frame()
        self.pack_forget()
    # endregion
