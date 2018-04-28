#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r
import bcrypt

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Check if an user and a password are correct
@rethinkdb_connection
def check_auth(args, conn):
    # Get the user
    if args["username"] and args["password"]:
        user = r.table("users").get(args["username"]).run(conn)

        # Check if the user exists
        if user:
            # Check if the password is correct
            return bcrypt.checkpw(args["password"].encode("utf-8"), user["password"].encode("utf-8"))

    return False


# Encrypt a password in order to store it to the DB
def encrypt_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
