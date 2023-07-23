import tkinter as tk

from ui.components.custom_vertical_input_field import CustomVerticalInputField


class MainMenuFrame(tk.Frame):
    __username_var: tk.StringVar
    __master_password_var: tk.StringVar

    def __init__(self, root: tk.Tk):
        self.__root = root
        super().__init__(self.__root, background="#2e3440")

        self.__username_var = tk.StringVar()
        self.__master_password_var = tk.StringVar()

        self.initialize_frame()

    def __get_x_center(self) -> int:
        self.__root.update()
        x = self.__root.winfo_width() / 2
        return int(x)

    def __get_y_center(self) -> int:
        self.__root.update()
        y = self.__root.winfo_height() / 2
        return int(y)

    def initialize_frame(self):
        # Username
        CustomVerticalInputField(self.__root, "Username", self.__username_var,
                                 x=self.__get_x_center(), y=self.__get_y_center(), y_offset=-100)

        # Username
        CustomVerticalInputField(self.__root, "Master Password", self.__master_password_var, show='ඞ',
                                 x=self.__get_x_center(), y=self.__get_y_center(), y_offset=-25)

        # region Submit
        submit_button = tk.Button(self.__root, text="Sign in", command=self.submit_command)
        submit_button.place(x=self.__get_x_center(), y=self.__get_y_center() + 70, anchor=tk.CENTER)
        # endregion

    # region Commands
    def submit_command(self):
        print(f"Submitted: {self.__username_var.get()}: {self.__master_password_var.get()}")
    # endregion
