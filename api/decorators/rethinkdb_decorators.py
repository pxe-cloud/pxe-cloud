#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Methods imports
from api.methods.rethinkdb_methods import connect, close


# Connect to the DB, execute the function and close the connection
def rethinkdb_connection(f):

    def wrapper(*args, **kwargs):
        conn = connect()

        # Execute the rest of the code
        try:
            result = f(conn, *args, **kwargs)

        except():
            return {"message": "Internal Server Error!"}, 500

        close(conn)

        return result

    return wrapper
