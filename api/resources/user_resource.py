#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Methods imports
from api.methods.files_methods import read_settings
from api.methods.rethinkdb_methods import connect
from api.methods.encryption_methods import encrypt_password


# User resource
class User(Resource):

    # GET
    def get(self, username):
        """
        Get a specific user using the username
        """
        rethink_settings = read_settings("rethinkdb")
        connect(r)
        user = r.db(rethink_settings["db_name"]).table("users").get(username).run()

        if user:
            return {"response": user}, 200

        else:
            return {"response": "Error 404! The user wasn't found!"}, 404

    # PUT
    def put(self, username):
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

        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("users").get(username).update(to_update).run()

        if result["replaced"] == 1:
            return {"response": "Successfully updated the user!"}, 200

        elif result["unchanged"] == 1:
            return {"response": "Error 400! Please make changes!"}, 400

        else:
            return {"response": "Error 404! User not found!"}, 404


    # DELETE
    def delete(self, username):
        """
        Delete an existing user using the username
        """
        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("users").get(username).delete().run()

        if result["deleted"] == 1:
            return {"response": "Successfully deleted the user!"}, 200

        else:
            return {"response": "Error 404! The user wasn't found!"}, 404
