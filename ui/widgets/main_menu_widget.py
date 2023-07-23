import tkinter as tk

import globals
from ui.components.custom_vertical_input_field import CustomVerticalInputField


class MainMenuWidget:
    # region Properties
    __root: tk.Tk
    __username_var: tk.StringVar
    __master_password_var: tk.StringVar
    # endregion

    # region Constructor
    def __init__(self):
        self.__root = tk.Tk()

        self.__username_var = tk.StringVar()
        self.__master_password_var = tk.StringVar()

        self.__initialize_widget()
        self.__initialize_components()
    # endregion

    # region UI
    def __initialize_widget(self):
        # region Set window position
        width = globals.MAIN_MENU_WIDGET_WIDTH
        height = globals.MAIN_MENU_WIDGET_HEIGHT
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.__root.geometry(f"{width}x{height}+{x}+{y}")
        # endregion

        # region Initializing Window
        self.__root.resizable(False, False)
        self.__root.title(globals.PROGRAM_NAME)
        self.__root.configure(bg='#2e3440')
        # TODO: Set window icon
        # endregion

    def __get_x_center(self) -> int:
        self.__root.update()
        x = self.__root.winfo_width() / 2
        return int(x)

    def __get_y_center(self) -> int:
        self.__root.update()
        y = self.__root.winfo_height() / 2
        return int(y)

    def __initialize_components(self):
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
    # endregion

    # region Commands
    def submit_command(self):
        print(f"Submitted: {self.__username_var.get()}: {self.__master_password_var.get()}")
    # endregion

    def show(self):
        self.__root.mainloop()
