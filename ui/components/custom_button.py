import tkinter as tk
import globals


class CustomButton(tk.Button):
    """Custom Button class. Derived from Tkinter Button"""

    def __init__(self, master: tk.Misc, text: str = None, command=None, button_size: int = globals.LARGE_BUTTON_SIZE,
                 x: int = 0, y: int = 0):
        """
        Custom Button constructor.

        :param master: The master (parent) component for the entry to be relative to.
        :param text: The text to show on the button.
        :param command: The command to execute when the button is clicked.
        :param button_size: The font size of the button text.
        :param x: The x position.
        :param y: The y position.
        """
        super().__init__(
            master=master,
            text=text,
            font=('calibre', button_size, 'normal'),
            justify="center",
            command=command,
            bg=globals.BUTTON_BG_COLOR,
            fg="#FFFFFF"
        )
        self.place(x=x, y=y, anchor=tk.CENTER)
