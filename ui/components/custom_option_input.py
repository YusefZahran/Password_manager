import tkinter as tk

import globals
from ui.components.custom_button import CustomButton
from ui.components.custom_option_menu import CustomOptionMenu


class CustomOptionInput:
    """Custom Option Input. Combines CustomOptionMenu and CustomButton to create a custom option input"""

    def __init__(self, master: tk.Misc, variable: tk.StringVar = None, options: [str] = None, button_text: str = None, seperation: int = -50, x: int = 0, y: int = 0):
        """
        :param master: The master (parent) component for the entry to be relative to
        :param variable: The linked variable with the input
        :param options: The options to show in the menu
        :param button_text: The text to show on the button
        :param x: The x position
        :param y: The y position
        """
        x_offset = x - seperation
        CustomOptionMenu(master, variable, options, x=x, y=y)
        CustomButton(master, button_text, button_size=globals.SMALL_BUTTON_SIZE, x=x_offset, y=y)
