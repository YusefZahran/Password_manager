import json
import PasswordManager

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


def write():
    pm = PasswordManager.PasswordManager()
    pw_json = json.dumps(pm.list_of_passwords)

    with open("notpasswords.json", "w") as outfile:
        outfile.write(pw_json)


def read():
    with open("notpasswords.json", "r") as infile:
        return json.load(infile)
