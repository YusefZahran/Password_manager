import tkinter as tk
from ui.components.custom_vertical_input_field import CustomVerticalInputField
from ui.frames.CustomFrame import CustomFrame


class MainMenuFrame(CustomFrame):
    # region Properties
    username_var: tk.StringVar
    master_password_var: tk.StringVar
    # endregion

    # region Constructor
    def __init__(self, master: tk.Misc):
        self.username_var = tk.StringVar()
        self.master_password_var = tk.StringVar()

        super().__init__(master)
    # endregion
    def switch_to_register(self):
        # Clear the current frame

        # Import and create the RegisterFrame to switch to it
        from ui.frames.Register_User_frame import RegisterUserFrame
        self.pack_forget()
        RegisterUserFrame(self.master).show()
        #RegisterUserFrame(self.master).pack()
        self.destroy_frame()
    #    self.destroy_frame()

    # region UI
    def initialize_frame(self):

        # Username
        CustomVerticalInputField(self, "Username", self.username_var,
                                 x=self._get_x_center(), y=self._get_y_center(), y_offset=-100)

        # Username
        CustomVerticalInputField(self, "Master Password", self.master_password_var, show='*',
                                 x=self._get_x_center(), y=self._get_y_center(), y_offset=-25)

        # region Submit
        submit_button = tk.Button(self, text="Don't have an account ?", command=self.switch_to_register)
        submit_button.place(x=self._get_x_center()+220, y=self._get_y_center() -180, anchor=tk.CENTER)

        submit_button = tk.Button(self, text="Sign in", command=self.submit_command)
        submit_button.place(x=self._get_x_center(), y=self._get_y_center()+70 , anchor=tk.CENTER)


        # endregion



    # endregion

    # region Commands
    def submit_command(self):
        print(f"Submitted: {self.username_var.get()}: {self.master_password_var.get()}")
        str_error = "Please fill in all the fields"
        lbl1 = "Login Successful! Welcome to the system!"
        lbl2 = "Username or password may be wrong "
        emptystr = ""
        while(self.username_var.get() == "" or self.master_password_var.get() == ""):
            error_label = tk.Label(self, text=str_error, fg="red")
            error_label.place(x=self._get_x_center(), y=self._get_y_center() + 100, anchor=tk.CENTER)
            print("Please fill in all the fields")
            return
            error_label = tk.Label(self, text=emptystr, fg="red")
            error_label.place(x=self._get_x_center(), y=self._get_y_center() + 100, anchor=tk.CENTER)

        username = self.username_var.get()
        password = self.master_password_var.get()
        self.show()
        from Registeration_Login import login
        if login(username, password):
            # Place code here that executes after successful login
            error_label = tk.Label(self, text=lbl1, fg="green")
            error_label.place(x=self._get_x_center(), y=self._get_y_center() + 100, anchor=tk.CENTER)

            return True

        else:
            # Place code here that executes when login fails
            error_label = tk.Label(self, text=lbl2, fg="red")
            error_label.place(x=self._get_x_center(), y=self._get_y_center() + 125, anchor=tk.CENTER)

        return False

        self.destroy_frame()
    # endregion
