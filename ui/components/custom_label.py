import tkinter as tk

import globals


class CustomLabel(tk.Label):

    def __init__(self, master: tk.Tk, text: str = None, x: int = 0, y: int = 0, x_offset: int = 0, y_offset: int = 0):
        super().__init__(master,
                         text=text,
                         justify="center",
                         foreground=globals.LABEL_FOREGROUND_COLOR,
                         background=globals.PROGRAM_BACKGROUND_COLOR)
        self.place(x=x + x_offset, y=y + y_offset, anchor=tk.CENTER)
