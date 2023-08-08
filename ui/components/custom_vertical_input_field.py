import tkinter as tk
from ui.components.custom_entry import CustomEntry
from ui.components.custom_label import CustomLabel


class CustomVerticalInputField:
    """Custom Vertical Input Field. Combines CustomLabel and CustomEntry to create a custom input field."""

    def __init__(self, master: tk.Misc, text: str = None, text_variable: tk.Variable = None, show: str = None,
                 separation: int = -25, x: int = 0, y: int = 0):
        """
        Custom Vertical Input Field constructor.

        :param master: The master (parent) component for the entry to be relative to.
        :param text: The text to display within the label.
        :param text_variable: The linked text variable with the input.
        :param show: The character to show instead of regular input characters.
        :param separation: The separation distance between the label and the entry.
        :param x: The x position.
        :param y: The y position.
        """
        y_offset = y - separation

        CustomLabel(master, text=text, x=x, y=y)

        CustomEntry(master, text_variable=text_variable, show=show, x=x, y=y_offset)
