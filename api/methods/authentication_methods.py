#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r
from api.methods.files_methods import read_settings
from api.methods.rethinkdb_methods import connect

# Check if an user and a password are correct
def check_auth(args):
    rethink_settings = read_settings("rethinkdb")
    connect(r)

    # Get the user
    users = r.db(rethink_settings["db_name"]).table("users").filter(r.row["username"] == args["username"]).run()

    # Loop through the cursor to get the user (and check if the user works)
    for user in users:

        # Check if the password is correct
        if user["password"] == args["password"]:
            return True

    return False
