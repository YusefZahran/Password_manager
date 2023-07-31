import tkinter as tk

import globals
from ui.components.custom_button import CustomButton
from ui.components.custom_entry import CustomEntry


class CustomSearchBar:
    """Custom Search Bar. Combines CustomEntry and CustomButton to create a custom search bar"""

    def __init__(self, master: tk.Misc, text_variable: tk.Variable = None, search_button_text = "Search",
                 show: str = None, separation: int = -95, x: int = 0, y: int = 0):
        """
        Custom Search bar constructor
        :param master: The master (parent) component for the entry to be relative to
        :param text_variable: The linked text variable with the input
        :param search_button_text: The text to show on the search button
        :param show: The character to show instead of regular input characters
        :param separation: The separation distance between the label and the entry
        :param x: The x position
        :param y: The y position
        """
        x_offset = x - separation

        CustomEntry(master, text_variable, show=show, x=x, y=y)

        CustomButton(master, search_button_text, x=x_offset, y=y)
