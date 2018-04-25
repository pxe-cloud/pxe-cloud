#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r
from api.methods.files_methods import read_settings
from api.methods.rethinkdb_methods import connect


# User resource
class User(Resource):

    # GET
    def get(self, username):
        """
        Get a specific user using  username
        """
        rethink_settings = read_settings("rethinkdb")
        connect(r)
        user = r.db(rethink_settings["db_name"]).table("users").get(username).run()

        if user:
            return user, 200

        else:
            return {"message": "Error 404! The user wasn't found!"}, 404

    # POST
    def post(self, username):
        """
        Create a new user
        """
        parser = reqparse.RequestParser()
        parser.add_argument("password", type=str, help="This is the password of the user")
        parser.add_argument("organization", type=str, help="This is the organization id that the user is going to be on")
        parser.add_argument("group", type=str, help="This is the group that the user is going to be on")
        args = parser.parse_args()

        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("users").insert([{
            "username": username,
            "password": args["password"],
            "organizations": [args["organization"]],
            "groups": [args["group"]]
        }]).run()

        if result["inserted"] == 1:
            return {"message": "Successfully created the user!"}, 201

        else:
            return {"message": "Error 409! The user already exists!"}, 409

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
                to_update[arg] = value

        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("users").get(username).update(to_update).run()

        if result["replaced"] == 1:
            return {"message": "Successfully updated the user!"}, 200

        elif result["unchanged"] == 1:
            return {"message": "Error 204! Please make changes!"}, 204

        else:
            return {"message": "Error 404! User not found!"}, 404


    # DELETE
    def delete(self, username):
        """
        Delete an existing user using the username
        """
        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("users").get(username).delete().run()

        if result["deleted"] == 1:
            return {"message": "Successfully deleted the user!"}, 200

        else:
            return {"message": "Error 404! The user wasn't found!"}, 404
