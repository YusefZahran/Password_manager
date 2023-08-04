import tkinter as tk

import globals
from account import Account
from ui.components.account_component import AccountComponent
from ui.components.custom_button import CustomButton
from ui.components.custom_option_input import CustomOptionInput
from ui.components.custom_search_bar import CustomSearchBar
from ui.frames.abstract_frame import AbstractFrame
from ui.frames.add_password_form import AddAccountFrame
from ui.frames.custom_frame import CustomFrame

# TODO: Make this not explode with too many tags
test_accounts_1 = [Account("Xacebook",
                           "codgamer69@yahoo.com",
                           "PASSWORD1",
                           ["fb", "meta", "codgamer"]),
                   Account("Twitter",
                           "mcgamer69@yahoo.com",
                           "PASSWORD2",
                           ["twitter", "x", "codgamer", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                            "n", "o"])]


class AccountsListFrame(AbstractFrame):
    """Accounts list frame"""
    # region Properties
    search_var: tk.StringVar
    """The search variable linked to the search bar"""
    sort_options = ["Title", "Username"]
    """The options in the sort menu"""
    filter_options = ["TEST TAG 1", "TEST TAG 2"]

    account_components: [AccountComponent] = []
    accounts: [Account] = []

    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        """Sign in form constructor
        :param master: The master (parent) component for the entry to be relative to
        """
        # Initialize UI variables
        self.filter_var = tk.StringVar()
        self.sort_var = tk.StringVar()
        self.search_var = tk.StringVar()
        self.list_canvas = None
        self.inner_frame = None

        # Parent constructor
        super().__init__(master)

    # endregion

    # region UI
    def initialize_frame(self):
        """Initializes the frame by drawing the components needed"""
        AccountsListFrame.accounts = test_accounts_1
        # Top bar elements
        top_bar = CustomFrame(self)
        top_bar.configure(width=globals.ROOT_WIDGET_WIDTH, height=50)

        # Search bar
        CustomSearchBar(top_bar, self.search_var, command=self.search_command, x=100, y=20)

        # Sort button
        CustomOptionInput(top_bar, self.sort_var, self.sort_options, "Sort", command=self.sort_command, x=300, y=20)

        # Filter button
        self.set_filter_options()
        CustomOptionInput(top_bar, self.filter_var, self.filter_options, "Filter", command=self.filter_command, x=420,
                          y=20)

        # Add account button
        CustomButton(top_bar, "Add Account", button_size=globals.SMALL_BUTTON_SIZE,
                     command=self.switch_to_add_account_frame, x=540, y=20)

        top_bar.pack()

        # Accounts list elements
        list_frame = tk.Frame(self, width=300, height=300)
        list_frame.pack(expand=True, fill=tk.BOTH)

        self.list_canvas = tk.Canvas(list_frame, bg=globals.PROGRAM_BACKGROUND_COLOR, highlightthickness=0,
                                     scrollregion=(0, 0, 500, 500))

        vbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        vbar.config(command=self.list_canvas.yview)

        self.list_canvas.config(width=300, height=300)
        self.list_canvas.config(yscrollcommand=vbar.set)

        # Create a frame inside the canvas to hold the AccountComponent widgets
        self.display_accounts(self.list_canvas, AccountsListFrame.accounts)

        # Update the scroll region based on the inner frame's size
        self.list_canvas.update_idletasks()
        self.list_canvas.config(scrollregion=self.list_canvas.bbox(tk.ALL))

        self.list_canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Bind the mouse scroll event to the canvas
        self.list_canvas.bind_all("<MouseWheel>",
                                  lambda event: self.list_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    def show(self):
        super().show()

    # endregion

    # region Commands
    def display_accounts(self, master: tk.Canvas, accounts: [Account]):
        master.delete(tk.ALL)
        self.inner_frame = tk.Frame(master)
        master.create_window(0, 0, window=self.inner_frame, anchor=tk.NW)

        for account in accounts:
            self.account_components.append(AccountComponent(self.inner_frame, account))
            self.account_components[-1].pack()

    def search_command(self):
        search_string = self.search_var.get().lower()
        if search_string == "":
            self.display_accounts(self.list_canvas, AccountsListFrame.accounts)
            return

        filtered_accounts = []
        for account in AccountsListFrame.accounts:
            if search_string in account.title.lower() \
                    or self.matches_pattern(search_string, account.username.lower()) \
                    or any(self.matches_pattern(search_string, detail.lower()) for detail in account.details):
                filtered_accounts.append(account)

        self.display_accounts(self.list_canvas, filtered_accounts)

    @staticmethod
    def matches_pattern(query, text):
        return text.startswith(query) or any(part.startswith(query) for part in text.split('@'))

    def sort_command(self):
        sort_by = self.sort_var.get()
        if sort_by == "-":
            self.display_accounts(self.list_canvas, AccountsListFrame.accounts)
            return

        sorted_accounts = []
        match sort_by:
            case "Title":
                sorted_accounts = sorted(AccountsListFrame.accounts, key=lambda account: account.title)
            case "Username":
                sorted_accounts = sorted(AccountsListFrame.accounts, key=lambda account: account.username)

        self.display_accounts(self.list_canvas, sorted_accounts)

    def set_filter_options(self):
        unique_details = set()
        for account in self.accounts:
            for detail in account.details:
                unique_details.add(detail)
        self.filter_options = list(unique_details)

    def filter_command(self):
        detail = self.filter_var.get()
        if detail == "-":
            self.display_accounts(self.list_canvas, AccountsListFrame.accounts)
            return
        filtered_accounts = []
        for account in AccountsListFrame.accounts:
            if detail in account.details:
                filtered_accounts.append(account)

        self.display_accounts(self.list_canvas, filtered_accounts)

    def switch_to_add_account_frame(self):
        self.pack_forget()
        self.destroy_frame()


    # endregion
