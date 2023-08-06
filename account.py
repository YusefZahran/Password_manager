import string


class Account:
    title: string
    username: string
    __password: string
    details: string = []

    def __init__(self, title, username, password, details=[ ]):
        self.title = title
        self.username = username
        self.__password = password
        self.details = details

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def __str__(self):
        return f"title: {self.title}\nusername: {self.username}\npassword: {self.__password}\ndetails: {self.details}\n"

    def edit_password(self,title, username,password,details=[ ]):
        self.title = title
        self.username = username
        self.set_password(password)
        self.details = details
