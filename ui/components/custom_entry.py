import tkinter as tk

import globals


class CustomEntry(tk.Entry):
    def __init__(self, master: tk.Misc, text_variable: tk.Variable = None, show: str = None, x: int = 0, y: int = 0,
                 x_offset: int = 0, y_offset: int = 0):
        super().__init__(master,
                         textvariable=text_variable,
                         font=('calibre', 10, 'normal'),
                         justify="center",
                         show=show,
                         background=globals.ENTRY_BG_COLOR,
                         foreground="#FFFFFF")
        self.place(x=x + x_offset, y=y + y_offset, anchor=tk.CENTER)
