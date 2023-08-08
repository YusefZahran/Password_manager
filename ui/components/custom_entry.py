import tkinter as tk
import globals


class CustomEntry(tk.Entry):
    """Custom Entry class. Derived from Tkinter Entry"""

    def __init__(self, master: tk.Misc, text_variable: tk.Variable = None, show: str = None, x: int = 0, y: int = 0):
        """
        Custom Entry constructor.

        :param master: The master (parent) component for the entry to be relative to.
        :param text_variable: The linked text variable with the input.
        :param show: The character to show instead of regular input characters.
        :param x: The x position.
        :param y: The y position.
        """
        super().__init__(
            master=master,
            textvariable=text_variable,
            font=globals.DEFAULT_FONT,
            justify="center",
            show=show,
            background=globals.ENTRY_BG_COLOR,
            foreground="#FFFFFF"
        )
        self.place(x=x, y=y, anchor=tk.CENTER)
