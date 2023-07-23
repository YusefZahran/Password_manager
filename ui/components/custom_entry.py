import tkinter as tk

import globals


class CustomEntry:
    entry: tk.Entry

    def __init__(self, root: tk.Tk, text_variable: tk.Variable = None, show: str = None, x: int = 0, y: int = 0,
                 x_offset: int = 0, y_offset: int = 0):
        entry = tk.Entry(root,
                         textvariable=text_variable,
                         font=('calibre', 10, 'normal'),
                         justify="center",
                         show=show,
                         background=globals.ENTRY_BG_COLOR,
                         foreground="#FFFFFF")
        entry.place(x=x + x_offset, y=y + y_offset, anchor=tk.CENTER)
        self.entry = entry
