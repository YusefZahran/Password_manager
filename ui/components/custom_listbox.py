import tkinter as tk

import globals
from ui.components.account_component import AccountComponent


class CustomAccountsListbox(tk.Listbox):
    """Custom Listbox class. Derived from Tkinter Listbox"""
    def __init__(self, master: tk.Misc, accounts: [AccountComponent] = None, x: int = 0, y: int = 0):
        """
        Custom Entry constructor
        :param master: The master (parent) component for the entry to be relative to
        :param accounts: The accounts in the listbox
        :param x: The x position
        :param y: The y position
        """
        super().__init__(master,
                         font=('calibre', 10, 'normal'),
                         justify="center",
                         activestyle='dotbox',
                         bg=globals.ENTRY_BG_COLOR,
                         fg="#FFFFFF")

        for account in accounts:
            self.insert(account.index, account)

        self.place(x=x, y=y, anchor=tk.CENTER)
