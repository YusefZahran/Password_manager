import tkinter as tk

import globals
from account import Account
from ui.components.custom_button import CustomButton
from ui.components.custom_label import CustomLabel
from ui.frames.abstract_frame import AbstractFrame
from ui.frames.custom_frame import CustomFrame


class AccountComponent(AbstractFrame):
    def __init__(self, master: tk.Misc, account: Account):
        self.account = account

        super().__init__(master)

    def initialize_frame(self):
        self.configure(padx=10, pady=10)

        frame = CustomFrame(self)
        frame.configure(padx=10, pady=20, highlightbackground=globals.FRAME_HIGHLIGHT_COLOR, highlightthickness=5)
        frame.pack()
        frame.bind("<Button-1>", self.show_account_info)

        CustomLabel(frame, self.account.title).grid(row=0, column=0, sticky=tk.W, pady=2, padx=25)

        CustomLabel(frame, self.account.username).grid(row=0, column=1, sticky=tk.W, pady=2, padx=25)

        col = 3
        for detail in self.account.details:
            CustomLabel(frame, detail).grid(row=0, column=col, sticky=tk.W, pady=5, padx=20)
            col += 1

    def show(self):
        self.pack()

    def show_account_info(self, click_event: tk.Event):
        # TODO: Show this account's info
        print(f"{self.account.title}")
