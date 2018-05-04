#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Groups resource
class Groups(Resource):

    # GET
    @rethinkdb_connection
    def get(self, conn):
        """
        Retrieve all the existing groups
        """
        groups = r.table("groups").run(conn)

        return {"response": [group for group in groups]}, 200

    # POST
    @rethinkdb_connection
    def post(self, conn):
        """
        Create a new group
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="This is the name of the group")
        parser.add_argument("description", type=str, help="This is a small description of the group")
        args = parser.parse_args()

        result = r.table("groups").insert([{
            "name": args["name"],
            "description": args["description"],
            "menu": ""
        }]).run(conn)

        if result["inserted"] == 1:
            return {"response": "Successfully created the group!"}, 201, {"Location": f"/group/{result['generated_keys'][0]}"}

        else:
            return {"response": "Error 500! Internal server error!"}, 500
