import string


class Password:
    title: string
    username: string
    __password: string
    details: string = []

    def __init__(self, title, username, password, details):
        self.title = title
        self.username = username
        self.__password = password
        self.details = details

    def __str__(self):
        return f"title: " + self.title + "\nusername: " + self.username + "\npassword: " + self.__password + \
            "\ndetails: " + self.details + "\n"
