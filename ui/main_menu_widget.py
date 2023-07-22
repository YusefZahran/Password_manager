import tkinter

import globals


class MainMenuWidget:
    root: tkinter.Tk

    def __init__(self):
        self.root = tkinter.Tk()

        # region Initializing Values

        # Get screen center
        width = globals.MAIN_MENU_WIDGET_WIDTH
        height = globals.MAIN_MENU_WIDGET_HEIGHT
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # endregion

        # region Initializing Window
        self.root.resizable = False
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        # endregion

    def show(self):
        self.root.mainloop()
