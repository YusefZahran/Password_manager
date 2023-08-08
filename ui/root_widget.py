import tkinter as tk
import globals
from ui.frames.abstract_frame import AbstractFrame


class RootWidget(tk.Tk):
    """The root widget for the application. Inherits from Tkinter Tk"""

    def __init__(self):
        """Root widget constructor"""
        super().__init__()
        self.__initialize_widget()

    def __initialize_widget(self):
        """Initializes the root widget by setting up the dimensions, location, and necessary components"""
        # Set window position
        width = globals.ROOT_WIDGET_WIDTH
        height = globals.ROOT_WIDGET_HEIGHT
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Initializing Window
        self.resizable(False, False)
        self.title(globals.PROGRAM_NAME)
        self.configure(bg=globals.PROGRAM_BACKGROUND_COLOR)

    def show(self):
        """Launches the root widget"""
        self.mainloop()

    def clear_canvas(self):
        """Clears the canvas by destroying all children"""
        for child in self.winfo_children():
            child.destroy()

    @staticmethod
    def add_frame(frame: tk.Frame | AbstractFrame):
        """Adds a frame to the root widget and initializes it"""
        if isinstance(frame, AbstractFrame):
            frame.show()
        else:
            frame.pack(expand=True, fill=tk.BOTH)
