#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Organization resource
class Organizations(Resource):

    # GET
    @rethinkdb_connection
    def get(self, conn):
        """
        Return all the existing organizations
        """
        organizations = r.table("organizations").run(conn)

        return {"response": [organization for organization in organizations]}, 200

    # POST
    @rethinkdb_connection
    def post(self, conn):
        """
        Create a new organization
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="This is the name of the organization")
        parser.add_argument("description", type=str, help="This is a small description of the organization")
        args = parser.parse_args()

        result = r.table("organizations").insert([{
            "name": args["name"],
            "description": args["description"],
            "groups": []
        }]).run(conn)

        if result["inserted"] == 1:
            return {"response": "Successfully created the organization!"}, 201, {"Location": f"/organization/{result['generated_keys'][0]}"}

        else:
            return {"response": "Error 500! Internal server error!"}, 500
