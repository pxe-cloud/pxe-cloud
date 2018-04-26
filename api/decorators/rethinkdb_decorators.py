#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Methods imports
import json
from api.methods.rethinkdb_methods import connect, close


# Connect to the DB, execute the function and close the connection
def rethinkdb_connection(f):

    def wrapper(*args, **kwargs):
        conn = connect()

        for arg in args:
            print(arg)

        # Execute the rest of the code
        print(type(args[0]))
        if type(args[0]) == dict:
            result = f(conn, *args, **kwargs)

        else:
            for index, vaule in enumerate(args[0]):
                print(index, vaule)
            # result = f(self, conn, **kwargs)
        try:
            pass

        except():
            return {"message": "Internal Server Error!"}, 500

        close(conn)

        return result

    return wrapper
