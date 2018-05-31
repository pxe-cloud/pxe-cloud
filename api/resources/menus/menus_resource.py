#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Menus resource
class Menus(Resource):

    # GET
    @rethinkdb_connection
    def get(self, conn):
        """
        Return all the existing menus
        """
        menus = r.table("menus").run(conn)

        return {"response": [menu for menu in menus]}, 200

    # POST
    @rethinkdb_connection
    def post(self, conn):
        """
        Create a new menu
        """
        parser = reqparse.RequestParser()
        parser.add_argument("title", required=True, type=str, help="This is the title of the menu")
        parser.add_argument("background", type=str, help="This is the background image of the menu")
        args = parser.parse_args()

        result = r.table("menus").insert([{
            "title": args["title"],
            "background": args["background"],
            "entries": []
        }]).run(conn)

        if result["inserted"] == 1:
            return {"response": "Successfully created the menu!"}, 201, {"Location": f"/menu/{result['generated_keys'][0]}"}

        else:
            return {"response": "Error 500! Internal server error!"}, 500
