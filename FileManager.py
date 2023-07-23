import json

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
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


<<<<<<< Updated upstream
def write(pw_dict):
    pw_dict = json.dumps(sample_passwords)

    with open("notpasswords.json", "w") as outfile:
        outfile.write(pw_dict)
=======
def write():
    pm = PasswordManager.PasswordManager()
    pw_json = json.dumps(pm.list_of_passwords)

    with open("notpasswords.json", "w") as outfile:
        outfile.write(pw_json)
>>>>>>> Stashed changes


def read():
    with open("notpasswords.json", "r") as infile:
        return json.load(infile)
