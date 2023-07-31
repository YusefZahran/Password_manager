import tkinter as tk

from ui.frames.abstract_frame import AbstractFrame
from ui.frames.account_frame import AccountFrame


class AccountsListFrame(AbstractFrame):
    """Accounts list frame"""
    # region Properties
    search_var: tk.StringVar
    """The search variable linked to the search bar"""

    accounts_lists: [AccountFrame]

    def __init__(self, master: tk.Misc):
        """Sign in form constructor
               :param master: The master (parent) component for the entry to be relative to
               """
        # Initialize UI variables
        self.search_var = tk.StringVar()

        # Parent constructor
        super().__init__(master)

    def initialize_frame(self):
        ...

    def show(self):
        super().show()
