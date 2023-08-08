import tkinter as tk
from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame

from globals import registered_users


class SignInFrame(CustomFrame):
    # region Properties
    username_var: tk.StringVar
    master_password_var: tk.StringVar
    is_logged_in: bool

    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        self.username_var = tk.StringVar()
        self.master_password_var = tk.StringVar()
        self.error_label = None
        self.is_logged_in = False
        super().__init__(master)

    # endregion
    def switch_to_register(self):
        # TODO: Fix this issue
        # Clear the current frame

        # Import and create the RegisterFrame to switch to it
        from ui.frames.register_user_frame import RegisterUserFrame
        self.pack_forget()
        RegisterUserFrame(self.master).show()
        self.destroy_frame()

    # region UI
    def initialize_frame(self):

        # Username
        CustomVerticalInputField(self, "Username", self.username_var,
                                 x=self.get_x_center(), y=self.get_y_center() - 100)

        # Username
        CustomVerticalInputField(self, "Master Password", self.master_password_var, show='ඞ',
                                 x=self.get_x_center(), y=self.get_y_center() - 25)

        # region Submit
        submit_button = tk.Button(self, text="Don't have an account ?", command=self.switch_to_register)
        submit_button.place(x=self.get_x_center() + 220, y=self.get_y_center() - 180, anchor=tk.CENTER)

        submit_button = tk.Button(self, text="Sign in", command=self.submit_command)
        submit_button.place(x=self.get_x_center(), y=self.get_y_center() + 70, anchor=tk.CENTER)

        # endregion

    # endregion

    # region Commands
    def submit_command(self):
        str_error = "Please fill in all the fields"
        lbl2 = "Username or password may be wrong "

        if self.username_var.get() == "" or self.master_password_var.get() == "":
            if self.error_label is not None:
                self.error_label.destroy()
            self.error_label = tk.Label(self, text=str_error, fg="red")
            self.error_label.place(x=self.get_x_center(), y=self.get_y_center() + 100, anchor=tk.CENTER)
            return

        username = self.username_var.get()
        password = self.master_password_var.get()
        self.show()

        if self.login(username, password):
            return True

        else:
            # Place code here that executes when login fails
            if self.error_label is not None:
                self.error_label.destroy()
            self.error_label = tk.Label(self, text=lbl2, fg="red")
            self.error_label.place(x=self.get_x_center(), y=self.get_y_center() + 125, anchor=tk.CENTER)

        # self.destroy_frame()
        return False

    # endregion

    def login(self, username, password):
        # Get user input for login credentials

        # Check if the entered username and password match the dictionary entries
        if username in registered_users and registered_users[username] == password:
            self.is_logged_in = True
            self.destroy_frame()
            return True
        else:
            self.is_logged_in = False
            return False
