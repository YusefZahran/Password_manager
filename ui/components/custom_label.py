import tkinter as tk

import globals


class CustomLabel(tk.Label):
    """Custom Label class. Derived from Tkinter Label"""
    def __init__(self, master: tk.Misc, text: str = None, x: int = 0, y: int = 0):
        """
        Custom Label constructor
        :param master: The master (parent) component for the entry to be relative to
        :param text: The text to display within the label
        :param x: The x position
        :param y: The y position
        """
        super().__init__(master,
                         text=text,
                         justify="center",
                         foreground=globals.LABEL_FOREGROUND_COLOR,
                         background=globals.PROGRAM_BACKGROUND_COLOR)
        self.place(x=x, y=y, anchor=tk.CENTER)
