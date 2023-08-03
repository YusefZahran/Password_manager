import tkinter as tk

from abc import ABC, abstractmethod

import globals


class AbstractFrame(tk.Frame, ABC):
    """Custom Frame. Derived from Tkinter Frame. Used to combine other components. Must be inherited from"""
    # region Constructor
    def __init__(self, master: tk.Misc):
        """Custom Frame constructor
        :param master: The master (parent) component for the entry to be relative to
        """
        super().__init__(master, background=globals.PROGRAM_BACKGROUND_COLOR)

        self.initialize_frame()

    # endregion

    # region UI
    def get_x_center(self) -> int:
        """Gets the x center of the master component"""
        self.master.update()
        x = self.master.winfo_width() / 2
        return int(x)

    def get_y_center(self) -> int:
        """Gets the y center of the master component"""
        self.master.update()
        y = self.master.winfo_height() / 2
        return int(y)

    @abstractmethod
    def initialize_frame(self):
        """Virtual function. Can be overridden by children.
        Must include the desired components to display within the frame"""
        pass

    @abstractmethod
    def show(self):
        """Virtual function. Can be overriden by children
        Must include how to show the frame"""
        self.pack(expand=True, fill=tk.BOTH)

    def destroy_frame(self):
        """Destroys the custom frame and all its children"""
        for child in self.winfo_children():
            child.destroy()

        self.destroy()
    # endregion
