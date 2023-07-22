from Cryptographer import Cryptographer


def cryptographer_test():
    username = "admin"
    master_password = "P@ssw0rd"

    cryptographer = Cryptographer(username, master_password)

    entry = "pass"
    token = cryptographer.encrypt_entry(entry)

    decrypted = cryptographer.decrypt_entry(token)

    print(decrypted)


def main():
    cryptographer_test()


if __name__ == '__main__':
    main()
