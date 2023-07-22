import tkinter as tk

import globals


class CustomLabel:
    label: tk.Label

    def __init__(self, root: tk.Tk, text: str = None, x: int = 0, y: int = 0,
                 x_offset: int = 0, y_offset: int = 0):
        label = tk.Label(root,
                         text=text,
                         justify="center",
                         foreground=globals.LABEL_FOREGROUND_COLOR)
        label.place(x=x + x_offset, y=y + y_offset, anchor=tk.CENTER)
        self.label = label
