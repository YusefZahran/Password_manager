import tkinter as tk

import globals
from ui.frames.main_menu_frame import MainMenuFrame


class RootWidget(tk.Tk):
    # region Constructor
    def __init__(self):
        super().__init__()
        self.__initialize_widget()

    # endregion

    # region UI
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
    def clear_canvas(self):
        for child in self.winfo_children():
            child.destroy()

    @staticmethod
    def add_frame(frame: tk.Frame | MainMenuFrame):
        if frame is tk.Frame:
            frame.pack(expand=True, fill=tk.BOTH)
        else:
            frame.show()

    # endregion
