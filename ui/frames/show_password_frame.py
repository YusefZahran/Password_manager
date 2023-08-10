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
        self.apply_button = None
        self.restore_title = None
        self.restore_username = None
        self.restore_password = None
        self.restore_details = None

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
        self.restore_title = tk.Button(self, text="Restore", command=lambda: self.restore_command("title"))
        self.restore_title.place(x=250, y=40)

        # Username info
        CustomLabel(self, text="Username: ", x=50, y=80)
        self.username_var_entry = CustomEntry(self, x=160, y=80)
        self.username_var_entry.insert(0, self.username_var)
        self.username_var_entry.configure(state="disabled")
        self.restore_username = tk.Button(self, text="Restore", command=lambda: self.restore_command("username"))
        self.restore_username.place(x=250, y=70)

        # Password info
        CustomLabel(self, text="Password: ", x=50, y=110)
        self.password_var_entry = CustomEntry(self, x=160, y=110)
        self.password_var_entry.insert(0, self.password_var)
        self.password_var_entry.configure(state="disabled")
        self.restore_password = tk.Button(self, text="Restore", command=lambda: self.restore_command("password"))
        self.restore_password.place(x=250, y=100)

        # Details info
        CustomLabel(self, text="Details: ", x=50, y=140)
        self.details_var_entry = CustomEntry(self, x=160, y=140)
        self.details_var_entry.insert(0, self.details_var)
        self.details_var_entry.configure(state="disabled")
        self.restore_details = tk.Button(self, text="Restore", command=lambda: self.restore_command("details"))
        self.restore_details.place(x=250, y=130)

        # Edit button
        self.edit_button = tk.Button(self, text="Edit", command=self.edit_command)
        self.edit_button.place(x=self.get_x_center(), y=self.get_y_center())

        # Apply button
        self.apply_button = tk.Button(self, text="Apply Changes", command=self.apply_command)


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
            self.edit_button.place(x=self.get_x_center() - 100, y=self.get_y_center())
            self.apply_button.place(x=self.get_x_center() + 40, y=self.get_y_center())


            self.is_edit = True
        else:
            self.title_var_entry.configure(state="disabled")
            self.username_var_entry.configure(state="disabled")
            self.password_var_entry.configure(state="disabled")
            self.details_var_entry.configure(state="disabled")
            self.edit_button.configure(text="Edit")
            self.edit_button.place(x=self.get_x_center(), y=self.get_y_center())
            self.apply_button.place_forget()

            self.is_edit = False



    def apply_command(self):
        old_file_name = globals.cryptographer.hash_entry(self.account.title)
        details_entry = self.details_var_entry.get().strip().split(", ")
        self.account.edit_account(self.title_var_entry.get(), self.username_var_entry.get(), self.password_var_entry.get(), details_entry)


        os.remove(f"{globals.CURRENT_USER_ACCOUNTS_DIR}/{old_file_name}.json")

        new_file_name = globals.cryptographer.hash_entry(self.title_var_entry.get())
        new_file_path = f"{globals.CURRENT_USER_ACCOUNTS_DIR}/{new_file_name}.json"

        data = globals.cryptographer.generate_data_from_entries(self.title_var_entry.get(),
                                                                self.username_var_entry.get(),
                                                                self.password_var_entry.get(),
                                                                self.details_var_entry.get())
        with open(new_file_path, "w") as f:
            json.dump(data, f)
    def exit_command(self):
        """Destroys the frame."""
        self.destroy_frame()

    def restore_command(self, arg):
        if arg == "title":
            self.title_var_entry.delete(0, "end")
            self.title_var_entry.insert(0, self.title_var)
        elif arg == "username":
            self.username_var_entry.delete(0, "end")
            self.username_var_entry.insert(0, self.username_var)
        elif arg == "password":
            self.password_var_entry.delete(0, "end")
            self.password_var_entry.insert(0, self.password_var)
        elif arg == "details":
            self.details_var_entry.delete(0, "end")
            self.details_var_entry.insert(0, self.details_var)
