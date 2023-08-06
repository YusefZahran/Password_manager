import tkinter as tk

import globals
from account import Account
from ui.components.account_component import AccountComponent
from ui.components.custom_button import CustomButton
from ui.components.custom_option_input import CustomOptionInput
from ui.components.custom_search_bar import CustomSearchBar
from ui.frames.abstract_frame import AbstractFrame
from ui.frames.custom_frame import CustomFrame


class AccountsListFrame(AbstractFrame):
    """Accounts list frame"""

    # region Properties
    __search_var: tk.StringVar
    """The search variable linked to the search bar"""
    __sort_options = ["Title", "Username"]
    """The options in the sort menu"""
    __filter_options = []
    """The options in the filter menu"""
    __account_components: [AccountComponent] = []
    """The accounts components list to display"""
    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        """Sign in form constructor
        :param master: The master (parent) component for the entry to be relative to
        """
        # Initialize UI variables
        self.filter_var = tk.StringVar()
        self.sort_var = tk.StringVar()
        self.__search_var = tk.StringVar()
        self.list_canvas = None
        self.inner_frame = None
        self.is_edit = False
        self.selected_account = None

        # Parent constructor
        super().__init__(master)
    # endregion

    # region UI
    def initialize_frame(self):
        """Initializes the frame by drawing the components needed"""
        # Top bar elements
        top_bar = CustomFrame(self)
        top_bar.configure(width=globals.ROOT_WIDGET_WIDTH, height=50)

        # Search bar
        CustomSearchBar(top_bar, self.__search_var, command=self.__search_command, x=100, y=20)

        # Sort button
        CustomOptionInput(top_bar, self.sort_var, self.__sort_options, "Sort", command=self.__sort_command, x=300, y=20)

        # Filter button
        self.__set_filter_options()
        CustomOptionInput(top_bar, self.filter_var, self.__filter_options, "Filter", command=self.__filter_command,
                          x=420, y=20)

        # Add account button
        CustomButton(top_bar, "Add Account", button_size=globals.SMALL_BUTTON_SIZE,
                     command=self.__add_account_frame_command, x=540, y=20)

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
        self.__display_accounts_command(self.list_canvas, globals.user_accounts)

        # Update the scroll region based on the inner frame's size
        self.list_canvas.update_idletasks()
        self.list_canvas.config(scrollregion=self.list_canvas.bbox(tk.ALL))

        self.list_canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Bind the mouse scroll event to the canvas
        self.list_canvas.bind_all("<MouseWheel>",
                                  lambda event: self.list_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    def show(self):
        """Shows the frame"""
        super().show()
    # endregion

    # region Commands
    def __display_accounts_command(self, master: tk.Canvas, accounts: [Account]):
        """Displays the accounts on the frame
        :param master: The master canvas to display the accounts on
        :param accounts: The accounts to display
        """
        master.delete(tk.ALL)
        self.inner_frame = tk.Frame(master)
        master.create_window(0, 0, window=self.inner_frame, anchor=tk.NW)

        row = 0

        for account in accounts:
            def func(a=account):
                return self.__edit_account_command(a)

            account_component = AccountComponent(self.inner_frame, account)
            account_component.grid(row=row, column=0, columnspan=2)
            btn = CustomButton(self.inner_frame, text="Edit Account", command=func)
            btn.grid(row=row, column=1)
            self.__account_components.append(account_component)
            row += 1

    def __search_command(self):
        """Searches the existing accounts for a match"""
        search_string = self.__search_var.get().lower()
        if search_string == "":
            self.__display_accounts_command(self.list_canvas, globals.user_accounts)
            return

        filtered_accounts = []
        for account in globals.user_accounts:
            if search_string in account.title.lower() \
                    or self.__matches_pattern(search_string, account.username.lower()) \
                    or any(self.__matches_pattern(search_string, detail.lower()) for detail in account.details):
                filtered_accounts.append(account)

        self.__display_accounts_command(self.list_canvas, filtered_accounts)

    @staticmethod
    def __matches_pattern(query, text):
        """Matches the email pattern"""
        return text.startswith(query) or any(part.startswith(query) for part in text.split('@'))

    def __sort_command(self):
        """Sorts the accounts displayed based on the chosen sort type"""
        sort_by = self.sort_var.get()
        if sort_by == "-":
            self.__display_accounts_command(self.list_canvas, globals.user_accounts)
            return

        sorted_accounts = []
        match sort_by:
            case "Title":
                sorted_accounts = sorted(globals.user_accounts, key=lambda account: account.title)
            case "Username":
                sorted_accounts = sorted(globals.user_accounts, key=lambda account: account.username)

        self.__display_accounts_command(self.list_canvas, sorted_accounts)

    def __set_filter_options(self):
        """Sets the filter option based on the chosen filter type"""
        try:
            unique_details = set()
            for account in globals.user_accounts:
                for detail in account.details:
                    unique_details.add(detail)
            self.__filter_options = list(unique_details)
        except Exception as e:
            print("An error occurred:", e)

    def __filter_command(self):
        """Filters the accounts displayed based on the chosen filter type"""
        detail = self.filter_var.get()
        if detail == "-":
            self.__display_accounts_command(self.list_canvas, globals.user_accounts)
            return
        filtered_accounts = []
        for account in globals.user_accounts:
            if detail in account.details:
                filtered_accounts.append(account)

        self.__display_accounts_command(self.list_canvas, filtered_accounts)

    def __add_account_frame_command(self):
        """Switches to the add account frame by destroying this frame"""
        self.is_edit = False
        self.pack_forget()
        self.destroy_frame()

    def __edit_account_command(self, account: Account):
        """Switches to the edit account frame by destroying this frame"""
        self.is_edit = True
        self.selected_account = account
        self.pack_forget()
        self.destroy_frame()
    # endregion
