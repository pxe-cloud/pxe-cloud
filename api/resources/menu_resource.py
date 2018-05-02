#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Menu resource
class Menu(Resource):

    # GET
    @rethinkdb_connection
    def get(self, menu_id, conn):
        """
        Get a specific menu using the id
        """
        menu = r.table("menus").get(menu_id).run(conn)

        if menu:
            return {"response": menu}, 200

        else:
            return {"response": "Error 404! The menu wasn't found!"}, 404

    # PUT
    @rethinkdb_connection
    def put(self, menu_id, conn):
        """
        Update an existing menu using the id
        """
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, help="This is the title of the menu")
        parser.add_argument("background", type=str, help="This is the background image of the menu")
        args = parser.parse_args()

        # Update only the parameters that are passed
        to_update = {}
        for arg, value in args.items():
            if value:
                to_update[arg] = value

        result = r.table("menus").get(menu_id).update(to_update).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully updated the menu!"}, 200

        elif result["unchanged"] == 1:
            return {"response": "Error 400! Please make some changes!"}, 400

        else:
            return {"response": "Error 404! Menu not found!"}, 404

    # DELETE
    @rethinkdb_connection
    def delete(self, menu_id, conn):
        """
        Delete an existing menu using the ID
        """
        result = r.table("menus").get(menu_id).delete().run(conn)

        if result["deleted"] == 1:
            return {"response": "Successfully deleted the menu!"}, 200

        else:
            return {"response": "Error 404! The menu wasn't found!"}, 404
