import tkinter as tk

from ui.frames.custom_frame import CustomFrame


class AccountFrame(CustomFrame):
    def __init__(self, master: tk.Misc):
        super().__init__(master)

    def initialize_frame(self):
        ...
