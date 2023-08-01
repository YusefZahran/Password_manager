import tkinter as tk

import globals
from ui.components.custom_button import CustomButton
from ui.components.custom_entry import CustomEntry


class CustomSearchBar:
    """Custom Search Bar. Combines CustomEntry and CustomButton to create a custom search bar"""

    def __init__(self, master: tk.Misc, text_variable: tk.Variable = None, command=None, search_button_text="Search",
                 separation: int = -95, x: int = 0, y: int = 0):
        """
        Custom Search bar constructor
        :param master: The master (parent) component for the entry to be relative to
        :param text_variable: The linked text variable with the input
        :param search_button_text: The text to show on the search button
        :param separation: The separation distance between the label and the entry
        :param x: The x position
        :param y: The y position
        """
        x_offset = x - separation

        CustomEntry(master,
                    text_variable,
                    x=x,
                    y=y)

        CustomButton(master,
                     search_button_text,
                     button_size=globals.SMALL_BUTTON_SIZE,
                     command=command,
                     x=x_offset,
                     y=y)
