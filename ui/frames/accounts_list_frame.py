import tkinter as tk

from ui.frames.abstract_frame import AbstractFrame
from ui.frames.account_frame import AccountFrame


class AccountsListFrame(AbstractFrame):
    accounts_lists: [AccountFrame]

    def __init__(self, master: tk.Misc):
        super().__init__(master)

    def initialize_frame(self):
        ...

    def show(self):
        super().show()
