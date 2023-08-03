import json
import password_manager

sample_passwords = {
    'passwords': [
        {
            "title": "Facebook",
            "username": "callofdutysexgamer100@yahoo.com",
            "__password": "password123",
            "details": ["important", "very important"]
        },
        {
            "title": "Twitter",
            "username": "callofdutysexgamer100@yahoo.com",
            "__password": "password123",
            "details": []
        }
    ]
}


class FileManager:
    @staticmethod
    def save_passwords():
        pm = password_manager.PasswordManager()
        # converts list of obj to list of dicts then to json
        pw_json = json.dumps([pw.__dict__ for pw in password_manager.list_of_passwords])

        with open("notpasswords.json", "w") as outfile:
            outfile.write(pw_json)

    @staticmethod
    def load_passwords():
        with open("notpasswords.json", "r") as infile:
            return json.load(infile)
