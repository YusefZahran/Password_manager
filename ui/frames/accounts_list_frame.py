import tkinter as tk

import globals
from ui.components.custom_button import CustomButton
from ui.components.custom_option_input import CustomOptionInput
from ui.components.custom_option_menu import CustomOptionMenu
from ui.components.custom_search_bar import CustomSearchBar
from ui.frames.abstract_frame import AbstractFrame
from ui.components.account_component import AccountComponent


class AccountsListFrame(AbstractFrame):
    """Accounts list frame"""
    # region Properties
    search_var: tk.StringVar
    """The search variable linked to the search bar"""
    sort_options = ["Name", "Date", "Tag"]
    """The options in the sort menu"""
    filter_options = ["TEST TAG 1", "TEST TAG 2"]

    accounts_lists: [AccountComponent]

    def __init__(self, master: tk.Misc):
        """Sign in form constructor
        :param master: The master (parent) component for the entry to be relative to
        """
        # Initialize UI variables
        self.filter_var = tk.StringVar()
        self.sort_var = tk.StringVar()
        self.search_var = tk.StringVar()

        # Parent constructor
        super().__init__(master)

    def initialize_frame(self):
        """Initializes the frame by drawing the components needed"""


        # Search bar
        CustomSearchBar(self, self.search_var, x=100, y=20)

        # Sort button
        CustomOptionInput(self, self.sort_var, self.sort_options, "Sort", x=300, y= 20)

        # Filter button
        CustomOptionInput(self, self.filter_var, self.filter_options, "Filter", x=420, y= 20)
        # Add account button
        CustomButton(self, "Add Account", button_size=globals.SMALL_BUTTON_SIZE, x=540, y= 20)

    def show(self):
        super().show()
