import tkinter as tk

from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.CustomFrame import CustomFrame


class MainMenuFrame(CustomFrame):
    # region Properties
    username_var: tk.StringVar
    master_password_var: tk.StringVar
    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        self.username_var = tk.StringVar()
        self.master_password_var = tk.StringVar()

        super().__init__(master)
    # endregion

    # region UI
    def initialize_frame(self):
        # Username
        CustomVerticalInputField(self, "Username", self.username_var,
                                 x=self._get_x_center(), y=self._get_y_center(), y_offset=-100)

        # Username
        CustomVerticalInputField(self, "Master Password", self.master_password_var, show='ඞ',
                                 x=self._get_x_center(), y=self._get_y_center(), y_offset=-25)

        # region Submit
        submit_button = tk.Button(self, text="Sign in", command=self.submit_command)
        submit_button.place(x=self._get_x_center(), y=self._get_y_center() + 70, anchor=tk.CENTER)
        # endregion

    # endregion

    # region Commands
    def submit_command(self):
        print(f"Submitted: {self.username_var.get()}: {self.master_password_var.get()}")
        self.destroy_frame()
    # endregion
