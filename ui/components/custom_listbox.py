import tkinter as tk
import globals
from ui.components.account_component import AccountComponent


class CustomAccountsListbox(tk.Listbox):
    """Custom Listbox class. Derived from Tkinter Listbox"""

    def __init__(self, master: tk.Misc, accounts: [str] = None, x: int = 0, y: int = 0):
        """
        Custom Listbox constructor.

        :param master: The master (parent) component for the entry to be relative to.
        :param accounts: The accounts in the listbox represented as a list of strings.
        :param x: The x position.
        :param y: The y position.
        """
        super().__init__(
            master,
            font=globals.DEFAULT_FONT,
            justify="center",
            activestyle='dotbox',
            bg=globals.ENTRY_BG_COLOR,
            fg="#FFFFFF"
        )

        if accounts:
            for account_text in accounts:
                self.insert(tk.END, account_text)

        self.place(x=x, y=y, anchor=tk.CENTER)
