from security import hash_password
from datetime import datetime


def log_activity(message):

    with open("activity.log", "a") as file:

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"[{time}] {message}\n")


def register(username, password):

    hashed = hash_password(password)

    try:

        with open("users.txt", "r") as file:

            users = file.readlines()

            for user in users:

                parts = user.strip().split("|")

                if parts[0] == username:

                    return False

    except:
        pass

    with open("users.txt", "a") as file:

        file.write(f"{username}|{hashed}\n")

    log_activity(f"{username} registered")

    return True


def login(username, password):

    hashed = hash_password(password)

    try:

        with open("users.txt", "r") as file:

            users = file.readlines()

            for user in users:

                parts = user.strip().split("|")

                if parts[0] == username and parts[1] == hashed:

                    log_activity(f"{username} logged in")

                    return True

    except:
        pass

    return False