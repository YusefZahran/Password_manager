import tkinter as tk
import globals
from ui.components.custom_button import CustomButton
from ui.components.custom_option_menu import CustomOptionMenu


class CustomOptionInput:
    """Custom Option Input. Combines CustomOptionMenu and CustomButton to create a custom option input."""

    def __init__(self, master: tk.Misc, variable: tk.StringVar = None, options: list[str] = None,
                 button_text: str = None, separation: int = 50, command=None, x: int = 0, y: int = 0):
        """
        Custom Option Input constructor.

        :param master: The master (parent) component for the entry to be relative to.
        :param variable: The linked variable with the input.
        :param options: The options to show in the menu.
        :param button_text: The text to show on the button.
        :param separation: The horizontal distance between the option menu and the button.
        :param command: The command to execute when the button is clicked.
        :param x: The x position.
        :param y: The y position.
        """
        x_offset = x + separation
        CustomOptionMenu(master, variable, options, x=x, y=y)
        CustomButton(master, button_text, command=command, button_size=globals.SMALL_BUTTON_SIZE, x=x_offset, y=y)
