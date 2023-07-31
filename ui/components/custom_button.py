import tkinter as tk

import globals


class CustomButton(tk.Button):
    """Custom Button class. Derived from Tkinter Button"""

    def __init__(self, master: tk.Misc, text: str = None, x: int = 0, y: int = 0):
        """
        Custom Button constructor
        :param master: The master (parent) component for the entry to be relative to
        :param text: The text to show on the button
        :param show: The character to show instead of regular input characters
        :param x: The x position
        :param y: The y position
        """
        super().__init__(master=master,
                         text=text,
                         font=('calibre', 7, 'normal'),
                         justify="center",
                         bg=globals.BUTTON_BG_COLOR,
                         fg="#FFFFFF")
        self.place(x=x, y=y, anchor=tk.CENTER)