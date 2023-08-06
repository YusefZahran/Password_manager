from ui.frames.sign_in_frame import SignInFrame
from ui.frames.accounts_list_frame import AccountsListFrame
from ui.frames.show_password_frame import ShowAccountFrame
from ui.frames.add_account_form import AddAccountFrame
from ui.root_widget import RootWidget


# region Main
def main():
    root = RootWidget()
    root.clear_canvas()

    main_menu = SignInFrame(root)
    root.add_frame(main_menu)
    root.wait_window(main_menu)
    while main_menu.is_logged_in:
        root.clear_canvas()
        account_list = AccountsListFrame(root)
        root.add_frame(account_list)
        root.wait_window(account_list)
        if account_list.is_edit:
            edit_account = ShowAccountFrame(root, account_list.selected_account)
            root.add_frame(edit_account)
            root.wait_window(edit_account)
        else:
            edit_account = AddAccountFrame(root)
            root.add_frame(edit_account)
            root.wait_window(edit_account)

    root.show()
    return 0


# endregion

# region Main
if __name__ == '__main__':
    main()
# endregion
