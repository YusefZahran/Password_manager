import tkinter as tk

import globals
from ui.components.account_component import AccountComponent
from ui.components.custom_button import CustomButton
from ui.components.custom_option_input import CustomOptionInput
from ui.components.custom_search_bar import CustomSearchBar
from ui.frames.abstract_frame import AbstractFrame
from ui.frames.custom_frame import CustomFrame


class AccountsListFrame(AbstractFrame):
    """Accounts list frame"""
    # region Properties
    search_var: tk.StringVar
    """The search variable linked to the search bar"""
    sort_options = ["Name", "Date", "Tag"]
    """The options in the sort menu"""
    filter_options = ["TEST TAG 1", "TEST TAG 2"]

    accounts_lists: [AccountComponent]

    # endregion

    # region Constructor
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

    # endregion

    # region UI
    def initialize_frame(self):
        """Initializes the frame by drawing the components needed"""

        # Top bar elements
        top_bar = CustomFrame(self)
        top_bar.configure(width=globals.ROOT_WIDGET_WIDTH, height=50)

        # Search bar
        CustomSearchBar(top_bar, self.search_var, command=self.search_command, x=100, y=20)

        # Sort button
        CustomOptionInput(top_bar, self.sort_var,  self.sort_options, "Sort", command=self.sort_command, x=300, y=20)

        # Filter button
        CustomOptionInput(top_bar, self.filter_var, self.filter_options, "Filter", command=self.filter_command, x=420, y=20)

        # Add account button
        CustomButton(top_bar, "Add Account", button_size=globals.SMALL_BUTTON_SIZE, command=self.switch_to_add_account_frame, x=540, y=20)

        top_bar.pack()

        # Accounts list elements
        accounts_list = CustomFrame(self)
        accounts_list.configure(width=globals.ROOT_WIDGET_WIDTH)
        AccountComponent(accounts_list, "Facebook", "codgamer69@yahoo.com", ["fb", "meta", "codgamer"]).pack()
        AccountComponent(accounts_list, "Facebook", "codgamer69@yahoo.com", ["fb", "meta", "codgamer"]).pack()
        AccountComponent(accounts_list, "Facebook", "codgamer69@yahoo.com", ["fb", "meta", "codgamer"]).pack()

        accounts_list.pack()

    def show(self):
        super().show()

    # endregion

    # region Commands
    def search_command(self):
        print("search: {}".format(self.search_var.get()))

    def sort_command(self):
        print("sort: {}".format(self.sort_var.get()))

    def filter_command(self):
        print("filter: {}".format(self.filter_var.get()))

    def switch_to_add_account_frame(self):
        print("switch")

    # endregion
