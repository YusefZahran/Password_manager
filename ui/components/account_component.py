import tkinter as tk
import globals
from account import Account
from ui.components.custom_label import CustomLabel
from ui.frames.abstract_frame import AbstractFrame
from ui.frames.custom_frame import CustomFrame


class AccountComponent(AbstractFrame):
    """Custom Account Component. Contains all UI elements related to an account"""

    def __init__(self, master: tk.Misc, account: Account):
        """
        Custom Account Component constructor.

        :param master: The master component.
        :param account: The account to be linked to this account component.
        """
        self.account = account
        super().__init__(master)

    def initialize_frame(self):
        """Initializes the frame by drawing the UI components."""
        self.configure(padx=20, pady=10)

        inner_frame = CustomFrame(self)
        inner_frame.configure(
            width=globals.ROOT_WIDGET_WIDTH - 50,
            height=75,
            padx=10,
            pady=20,
            highlightbackground=globals.FRAME_HIGHLIGHT_COLOR,
            highlightthickness=5
        )
        inner_frame.pack()

        frame_y_center = 15

        CustomLabel(inner_frame, text=self.account.title, justify="left").place(x=30, y=frame_y_center)

        CustomLabel(inner_frame, text=self.account.username, justify="left").place(x=155, y=frame_y_center)

    def show(self):
        """Shows the AccountComponent frame."""
        self.pack()
