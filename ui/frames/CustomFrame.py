import tkinter as tk

from abc import ABC, abstractmethod

import globals


class CustomFrame(tk.Frame, ABC):
    # region Constructor
    def __init__(self, master: tk.Misc):
        super().__init__(master, background=globals.PROGRAM_BACKGROUND_COLOR)

        self.initialize_frame()

    # endregion

    # region UI
    def _get_x_center(self) -> int:
        self.master.update()
        x = self.master.winfo_width() / 2
        return int(x)

    def _get_y_center(self) -> int:
        self.master.update()
        y = self.master.winfo_height() / 2
        return int(y)

    @abstractmethod
    def initialize_frame(self):
        pass

    def show(self):
        self.pack(expand=True, fill=tk.BOTH)

    def destroy_frame(self):
        for child in self.winfo_children():
            child.destroy()

        self.destroy()
    # endregion
