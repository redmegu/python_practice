def check_username():
    username = input("Select a username: ")
    if len(username) < 4:
        print("The username must be at least 4 characters.")
    else:
        print("Your username is valid!")

check_username()