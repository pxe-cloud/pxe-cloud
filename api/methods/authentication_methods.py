#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Check if an user and a password are correct
@rethinkdb_connection
def check_auth(args, conn):

    # Get the user
    users = r.table("users").filter(r.row["username"] == args["username"]).run(conn)

    # Loop through the cursor to get the user (and check if the user works)
    for user in users:

        # Check if the password is correct
        if user["password"] == args["password"]:
            return True

    return False
