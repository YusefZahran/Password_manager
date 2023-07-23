import tkinter as tk

import globals


class RootWidget(tk.Tk):
    # region Constructor
    def __init__(self):
        super().__init__()
        self.__initialize_widget()
    # endregion

    # region Root UI
    def __initialize_widget(self):
        # region Set window position
        width = globals.MAIN_MENU_WIDGET_WIDTH
        height = globals.MAIN_MENU_WIDGET_HEIGHT
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")
        # endregion

        # region Initializing Window
        self.resizable(False, False)
        self.title(globals.PROGRAM_NAME)
        self.configure(bg=globals.PROGRAM_BACKGROUND_COLOR)
        # TODO: Set window icon
        # endregion

    def show(self):
        self.mainloop()
    # endregion

    # region Frames
    @staticmethod
    def add_frame(frame: tk.Frame):
        frame.pack()

    # endregion
