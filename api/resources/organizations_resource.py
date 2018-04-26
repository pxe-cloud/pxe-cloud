#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Methods imports
from api.methods.files_methods import read_settings
from api.methods.rethinkdb_methods import connect

# Organization resource
class Organizations(Resource):
    # GET
    def get(self):
        """
        Return all the existing organizations
        """
        rethink_settings = read_settings("rethinkdb")
        connect(r)
        organizations = r.db(rethink_settings["db_name"]).table("organizations").run()

        return {"response": [organization for organization in organizations]}, 200

    # POST
    def post(self):
        """
        Create a new organization
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="This is the name of the organization")
        parser.add_argument("description", type=str, help="This is a small description of the organization")
        args = parser.parse_args()

        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("organizations").insert([{
            "name": args["name"],
            "description": args["description"],
            "groups": []
        }]).run()

        if result["inserted"] == 1:
            return {"response": "Successfully created the organization!"}, 201, {"Location": f"/organization/{result['generated_keys'][0]}"}

        else:
            return {"response": "Error 500! Internal server error!"}, 500
