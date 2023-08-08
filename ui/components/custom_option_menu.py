import tkinter as tk

import globals


class CustomOptionMenu(tk.OptionMenu):
    """Custom Option Menu class. Derived from Tkinter OptionMenu"""

    def __init__(self, master: tk.Misc, variable: tk.StringVar = None, options: [str] = None, x: int = 0, y: int = 0):
        """
        Custom Option Menu constructor.

        :param master: The master (parent) component for the entry to be relative to.
        :param variable: The linked variable with the input.
        :param options: The options to show in the menu.
        :param x: The x position.
        :param y: The y position.
        """
        super().__init__(master,
                         variable,
                         "-",
                         *options
                         )
        # Default value
        variable.set("-")  # Set the default value if options are available
        self.config(
            font=('calibre', globals.SMALL_BUTTON_SIZE, 'normal'),
            justify="center",
            background=globals.ENTRY_BG_COLOR,
            foreground="#FFFFFF",
            activebackground="#FFFFFF",
            activeforeground=globals.ENTRY_BG_COLOR,
            highlightthickness=0,
            bd=1,
            indicatoron=False,
            height=1,
            width=10
        )
        self.place(x=x, y=y, anchor=tk.CENTER)
