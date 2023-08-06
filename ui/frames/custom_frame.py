import tkinter as tk

from ui.frames.abstract_frame import AbstractFrame


class CustomFrame(AbstractFrame):
    """Base skeleton for a custom frame. Derived from Abstract Frame"""
    def __init__(self, master: tk.Misc):
        """Custom frame constructor
        :param master: The master component
        """
        super().__init__(master)
    # endregion

    def initialize_frame(self):
        """Initializes the frame. Empty function"""
        pass

    def show(self):
        """Shows the frame by packing it with specific parameters"""
        self.pack(expand=True, fill=tk.BOTH)
