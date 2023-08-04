import tkinter as tk

import globals
from account import Account
from ui.components.custom_label import CustomLabel
from ui.frames.abstract_frame import AbstractFrame
from ui.frames.custom_frame import CustomFrame


class AccountComponent(AbstractFrame):
    def __init__(self, master: tk.Misc, account: Account):
        self.account = account

        super().__init__(master)

    def initialize_frame(self):
        self.configure(padx=20, pady=10)

        inner_frame = CustomFrame(self)
        inner_frame.configure(width=globals.ROOT_WIDGET_WIDTH - 50, height=75, padx=10, pady=20,
                              highlightbackground=globals.FRAME_HIGHLIGHT_COLOR, highlightthickness=5)
        inner_frame.pack()
        # inner_frame.bind("<Button-1>", self.show_account_info)

        frame_y_center = 15

        CustomLabel(inner_frame, self.account.title, "left").place(x=30, y=frame_y_center)

        CustomLabel(inner_frame, self.account.username, "left").place(x=155, y=frame_y_center)

    def show(self):
        self.pack()

    def show_account_info(self, click_event: tk.Event):
        # TODO: Show this account's info
        print(f"{self.account.title}")
