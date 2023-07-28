import tkinter as tk

from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.CustomFrame import CustomFrame


class RegisterUserFrame(CustomFrame):
    # region Properties
    registered_username: tk.StringVar
    registered_password: tk.StringVar
    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        self.registered_username = tk.StringVar()
        self.registered_password = tk.StringVar()

        super().__init__(master)
    # endregion

    # region UI
    def initialize_frame(self):
        # Username
        CustomVerticalInputField(self, "Username", self.registered_username,
                                 x=self._get_x_center(), y=self._get_y_center(), y_offset=-100)

        # Username
        CustomVerticalInputField(self, "Master Password", self.registered_password, show='ඞ',
                                 x=self._get_x_center(), y=self._get_y_center(), y_offset=-25)

        # region Submit
        submit_button = tk.Button(self, text="Sign Up", command=self.submit_command)
        submit_button.place(x=self._get_x_center(), y=self._get_y_center() + 70, anchor=tk.CENTER)
        # endregion

    # endregion

    # region Commands
    def submit_command(self):
        print(f"Submitted: {self.registered_username.get()}: {self.registered_password.get()}")
        self.destroy_frame()
    # endregion
