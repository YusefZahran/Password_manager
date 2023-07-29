import tkinter as tk

from ui.frames.account_frame import AccountFrame
from ui.frames.custom_frame import CustomFrame


class AccountsListFrame(CustomFrame):
    accounts_lists: [AccountFrame]

    def __init__(self, master: tk.Misc):
        super().__init__(master)

    def initialize_frame(self):
        ...
