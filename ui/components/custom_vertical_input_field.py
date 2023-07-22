import tkinter as tk

import globals
from ui.components.custom_entry import CustomEntry
from ui.components.custom_label import CustomLabel


class CustomVerticalInputField:
    custom_label: CustomLabel
    custom_entry: CustomEntry

    def __init__(self, root: tk.Tk, text: str = None, text_variable: tk.Variable = None, show: str = None,
                 separation: int = -25, x: int = 0, y: int = 0,
                 x_offset: int = 0, y_offset: int = 0):
        entry_y_offset = y_offset - separation

        self.custom_label = CustomLabel(root, text,
                                        x=x, y=y, x_offset=x_offset, y_offset=y_offset)

        self.custom_entry = CustomEntry(root, text_variable, show=show,
                                        x=x, y=y, x_offset=x_offset, y_offset=entry_y_offset)
