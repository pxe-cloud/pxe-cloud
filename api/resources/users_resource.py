#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Methods imports
from api.methods.files_methods import read_settings
from api.methods.rethinkdb_methods import connect
from api.methods.encryption_methods import encrypt_password


# Users resource
class Users(Resource):

    # GET
    def get(self):
        """
        Return all the existing users
        """
        rethink_settings = read_settings("rethinkdb")
        connect(r)
        users = r.db(rethink_settings["db_name"]).table("users").run()

        return {"response": [user for user in users]}, 200

    # POST
    def post(self):
        """
        Create a new user
        """
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="This is the username of the user")
        parser.add_argument("password", type=str, help="This is the password of the user")
        parser.add_argument("organization", type=str, help="This is the organization id that the user is going to be on")
        parser.add_argument("group", type=str, help="This is the group that the user is going to be on")
        args = parser.parse_args()

        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("users").insert([{
            "username": args["username"],
            "password": encrypt_password(args["password"]),
            "organizations": [args["organization"]],
            "groups": [args["group"]]
        }]).run()

        if result["inserted"] == 1:
            return {"response": "Successfully created the user!"}, 201, {"Location": f"/user/{result['generated_keys'][0]}"}

        else:
            return {"response": "Error 409! The user already exists!"}, 409
