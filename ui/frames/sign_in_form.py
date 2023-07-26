import tkinter as tk

from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.custom_frame import CustomFrame


class SignInForm(CustomFrame):
    """Sign in form frame"""
    # region Properties
    username_var: tk.StringVar
    """The username variable linked to the username entry"""
    master_password_var: tk.StringVar
    """The master password variable linked to the username entry"""
    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        """Sign in form constructor
        :param master: The master (parent) component for the entry to be relative to
        """
        # Initialize UI variables
        self.username_var = tk.StringVar()
        self.master_password_var = tk.StringVar()

        # Parent constructor
        super().__init__(master)
    # endregion

    # region UI
    def initialize_frame(self):
        """Initializes the frame by drawing the components needed"""
        # Username Field
        CustomVerticalInputField(self, "Username", self.username_var,
                                 x=self._get_x_center(), y=self._get_y_center() - 100)

        # Master Password Field
        CustomVerticalInputField(self, "Master Password", self.master_password_var, show='ඞ',
                                 x=self._get_x_center(), y=self._get_y_center() - 25)

        # region Submit
        submit_button = tk.Button(self, text="Sign in", command=self.submit_command)
        submit_button.place(x=self._get_x_center(), y=self._get_y_center() + 70, anchor=tk.CENTER)
        # endregion

    # endregion

    # region Commands
    def submit_command(self):
        """Submit command. Prints the submitted info"""
        print(f"Submitted: {self.username_var.get()}: {self.master_password_var.get()}")
        self.destroy_frame()
    # endregion
