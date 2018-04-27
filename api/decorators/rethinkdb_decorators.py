#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Methods imports
import json
from api.methods.rethinkdb_methods import connect, close


# Connect to the DB, execute the function and close the connection
def rethinkdb_connection(f):

    def wrapper(*args, **kwargs):
        conn = connect()

        # Execute the rest of the code
        try:
            result = f(*args, conn=conn, **kwargs)

        except():
            return {"response": "Error 503! The database is unaccessible!"}, 503

        close(conn)

        return result

    return wrapper
