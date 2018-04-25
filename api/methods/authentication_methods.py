# Check if an user and a password are correct
def check_auth(args):
    users = {"user": "1234"}

    # Check if the user exists
    if args["username"] in users:

        # Check if the password is correct
        if users[args["username"]] == args["password"]:
            return True

    return False
