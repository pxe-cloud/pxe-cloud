#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r
import bcrypt

from api.methods.files_methods import read_settings
from api.methods.rethinkdb_methods import connect


# Check if an user and a password are correct
def check_auth(args):
    rethink_settings = read_settings("rethinkdb")
    connect(r)

    # Get the user
    if args["username"] and args["password"]:
        user = r.db(rethink_settings["db_name"]).table("users").get(args["username"]).run()

        # Check if the user exists
        if user:
            # Check if the password is correct
            return bcrypt.checkpw(args["password"].encode("utf-8"), user["password"].encode("utf-8"))

    return False


# Encrypt a password in order to store it to the DB
def encrypt_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
