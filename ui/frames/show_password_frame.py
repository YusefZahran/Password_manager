import hashlib
import json
import os
import tkinter as tk
import globals
from account import Account
from ui.frames.custom_frame import CustomFrame
from ui.components.custom_label import CustomLabel
from ui.components.custom_entry import CustomEntry


class ShowAccountFrame(CustomFrame):
    """Show Password Form Frame"""

    def __init__(self, master: tk.Misc, account: Account):
        """
        Show Account Frame constructor.

        :param master: The master component.
        :param account: The Account object to display.
        """
        # initializing account values
        self.account = account
        self.title_var = account.title
        self.username_var = account.username
        self.password_var = account.get_password()
        self.details_var = ", ".join(account.details)

        # initializing entries
        self.title_var_entry = None
        self.username_var_entry = None
        self.password_var_entry = None
        self.details_var_entry = None

        # initializing buttons
        self.edit_button = None
        self.exit_button = None

        self.is_edit = False

        super().__init__(master)

    def initialize_frame(self):
        """Initializes the frame by drawing UI components."""
        # Frame title
        CustomLabel(self, text="Account Information: ", x=300, y=20)

        # Title info
        CustomLabel(self, text="Title: ", x=50, y=50)
        self.title_var_entry = CustomEntry(self, x=160, y=50)
        self.title_var_entry.insert(0, self.title_var)
        self.title_var_entry.configure(state="disabled")

        # Username info
        CustomLabel(self, text="Username: ", x=50, y=80)
        self.username_var_entry = CustomEntry(self, x=160, y=80)
        self.username_var_entry.insert(0, self.username_var)
        self.username_var_entry.configure(state="disabled")

        # Password info
        CustomLabel(self, text="Password: ", x=50, y=110)
        self.password_var_entry = CustomEntry(self, x=160, y=110)
        self.password_var_entry.insert(0, self.password_var)
        self.password_var_entry.configure(state="disabled")

        # Details info
        CustomLabel(self, text="Details: ", x=50, y=140)
        self.details_var_entry = CustomEntry(self, x=160, y=140)
        self.details_var_entry.insert(0, self.details_var)
        self.details_var_entry.configure(state="disabled")

        # Edit button
        self.edit_button = tk.Button(self, text="Edit", command=self.edit_command)
        self.edit_button.place(x=self.get_x_center(), y=self.get_y_center())

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_command)
        self.exit_button.place(x=self.get_x_center(), y=self.get_y_center() + 50)

    def edit_command(self):
        """Toggles the edit mode for the entries."""
        if not self.is_edit:
            self.title_var_entry.configure(state="normal")
            self.username_var_entry.configure(state="normal")
            self.password_var_entry.configure(state="normal")
            self.details_var_entry.configure(state="normal")
            self.edit_button.configure(text="Show")
            self.is_edit = True
        else:
            self.title_var_entry.configure(state="disabled")
            self.username_var_entry.configure(state="disabled")
            self.password_var_entry.configure(state="disabled")
            self.details_var_entry.configure(state="disabled")
            self.edit_button.configure(text="Edit")
            self.is_edit = False

            # TODO: Remove and fix dulicates
            data = globals.cryptographer.encrypt_entry(self.title_var_entry.get()).decode('utf-8') + "\n"
            data += globals.cryptographer.encrypt_entry(self.username_var_entry.get()).decode('utf-8') + "\n"
            data += globals.cryptographer.encrypt_entry(self.password_var_entry.get()).decode('utf-8') + "\n"
            data += globals.cryptographer.encrypt_entry(','.join(self.details_var_entry.get())).decode('utf-8')

            new_file_name = hashlib.sha256()
            new_file_name.update(bytes(self.title_var_entry.get(), 'utf-8'))
            new_file_name = new_file_name.hexdigest()

            new_file_path = f"{globals.CURRENT_USER_ACCOUNTS_DIR}/{new_file_name}.json"

            # data = globals.cryptographer.generate_data_from_entries(self.title_var_entry.get(),
            #                                                         self.username_var_entry.get(),
            #                                                         self.password_var_entry.get(),
            #                                                         ','.join(self.details_var_entry.get()))
            with open(new_file_path, "w") as f:
                json.dump(data, f)

            old_file_name = hashlib.sha256()
            old_file_name.update(bytes(self.account.title, 'utf-8'))
            old_file_name = old_file_name.hexdigest()
            os.remove(f"{globals.CURRENT_USER_ACCOUNTS_DIR}/{old_file_name}.json")

    def exit_command(self):
        """Destroys the frame."""
        self.destroy_frame()
