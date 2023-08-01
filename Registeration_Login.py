import tkinter
from ui.frames.main_menu_frame import MainMenuFrame
from ui.frames.Register_User_frame import RegisterUserFrame
from ui.root_widget import RootWidget



# region Registration
# Dictionary to store registered users' credentials
registered_users = {}


def register_user(Username , String):
    # Get user input for username and password
    username = Username
    password = String

    # Save the username and password in the dictionary
    registered_users[username] = password

    print("Registration Successful!")
    return 0


def login(username,password):
    # Get user input for login credentials

    # Check if the entered username and password match the dictionary entries
    if username in registered_users and registered_users[username] == password:
        print("Login Successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False



def ui_test_register():
    root = RootWidget()
    root.clear_canvas()

    reg_screen = RegisterUserFrame(root)
    root.add_frame(reg_screen)
    root.wait_window(reg_screen)
    #print(f"Received: {reg_screen.registered_username.get()}: {reg_screen.registered_password.get()}")
    username =reg_screen.registered_username.get()
    password =reg_screen.registered_password.get()
    register_user(username,password)
    root.show()
    #root.destroy()

def ui_login():
    root = RootWidget()
    root.clear_canvas()

    main_menu = MainMenuFrame(root)
    root.add_frame(main_menu)
    root.wait_window(main_menu)
    # print(f"Received: {main_menu.username_var.get()}: {main_menu.master_password_var.get()}")
    username = main_menu.username_var.get()
    password = main_menu.master_password_var.get()
    root.show()
    if login(username, password):
        # Place code here that executes after successful login
        return True
    else:
        # Place code here that executes when login fails
        return False
    root.destroy()

