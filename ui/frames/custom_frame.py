import tkinter as tk

from ui.frames.abstract_frame import AbstractFrame


class CustomFrame(AbstractFrame):
    def __init__(self, master: tk.Misc):
        super().__init__(master)
    # endregion

    def initialize_frame(self):
        pass

    def show(self):
        self.pack(expand=True, fill=tk.BOTH)
