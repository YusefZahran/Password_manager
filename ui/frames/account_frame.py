import tkinter as tk

import globals
from ui.components.custom_label import CustomLabel
from ui.frames.abstract_frame import AbstractFrame
from ui.frames.custom_frame import CustomFrame


class AccountFrame(AbstractFrame):
    def __init__(self, master: tk.Misc, name: str, username: str, tags: [str]):
        self.name = name
        self.username = username
        self.tags = tags

        super().__init__(master)

    def initialize_frame(self):
        self.configure(padx=10, pady=10)

        frame = CustomFrame(self)
        frame.configure(padx=50, pady=20, width=globals.ROOT_WIDGET_WIDTH - 50, height=50,
                        highlightbackground=globals.FRAME_HIGHLIGHT_COLOR, highlightthickness=5)
        frame.pack()

        CustomLabel(frame, self.name).grid(row=0, column=0, sticky=tk.W, pady=2)

        CustomLabel(frame, self.username).grid(row=0, column=1, sticky=tk.W, pady=2, padx=25)

        col = 3
        for tag in self.tags:
            CustomLabel(frame, tag).grid(row=0, column=col, sticky=tk.W, pady=5, padx=2)
            col += 1

    def show(self):
        self.pack()


