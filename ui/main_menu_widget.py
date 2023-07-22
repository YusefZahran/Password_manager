import tkinter

import globals


class MainMenuWidget:
    def __init__(self):
        root = tkinter.Tk()

        # region Initializing Values

        # Get screen center
        width = globals.MAIN_MENU_WIDGET_WIDTH
        height = globals.MAIN_MENU_WIDGET_HEIGHT
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        # endregion

        # region Initializing Window
        root.resizable = False
        root.geometry(f"{width}x{height}+{x}+{y}")
        # endregion

        root.mainloop()
