#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection

# Methods imports
from api.methods.encryption_methods import encrypt_password


# User resource
class User(Resource):

    # GET
    @rethinkdb_connection
    def get(self, username, conn):
        """
        Get a specific user using the username
        """
        user = r.table("users").get(username).run(conn)

        if user:
            return {"response": user}, 200

        else:
            return {"response": "Error 404! The user wasn't found!"}, 404

    # PUT
    @rethinkdb_connection
    def put(self, username, conn):
        """
        Update an existing user using the username
        """
        parser = reqparse.RequestParser()
        parser.add_argument("password", type=str, help="This is the password of the user")
        parser.add_argument("organization", type=str, help="This is the organization id that the user is going to be on")
        parser.add_argument("group", type=str, help="This is the group that the user is going to be on")
        args = parser.parse_args()

        # Update only the parameters that are passed
        to_update = {}
        for arg, value in args.items():
            if value:
                if arg == "password":
                    to_update[arg] = encrypt_password(value)

                else:
                    to_update[arg] = value

        result = r.table("users").get(username).update(to_update).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully updated the user!"}, 200

        elif result["unchanged"] == 1:
            return {"response": "Error 400! Please make changes!"}, 400

        else:
            return {"response": "Error 404! User not found!"}, 404


    # DELETE
    @rethinkdb_connection
    def delete(self, username, conn):
        """
        Delete an existing user using the username
        """
        result = r.table("users").get(username).delete().run(conn)

        if result["deleted"] == 1:
            return {"response": "Successfully deleted the user!"}, 200

        else:
            return {"response": "Error 404! The user wasn't found!"}, 404
