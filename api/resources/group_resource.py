#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Group Resource
class Group(Resource):

    # GET
    @rethinkdb_connection
    def get(self, group_id, conn):
        """
        Get a specific group using an id
        """
        group = r.table("groups").get(group_id).run(conn)

        if group:
            return {"response": group}, 200

        else:
            return {"response": "Error 404! The group wasn't found!"}, 404

    # PUT
    @rethinkdb_connection
    def put(self, group_id, conn):
        """
        Update an existing group using the ID
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="This is the name of the group")
        parser.add_argument("description", type=str, help="This is a small description of the group")
        args = parser.parse_args()

        # Update only the parameters that are passed
        to_update = {}
        for arg, value in args.items():
            if value:
                to_update[arg] = value

        result = r.table("groups").get(group_id).update(to_update).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully updated the group!"}, 200

        elif result["unchanged"] == 1:
            return {"response": "Error 400! Please make some changes!"}, 400

        else:
            return {"response": "Error 404! Group not found!"}, 404

    # DELETE
    @rethinkdb_connection
    def delete(self, group_id, conn):
        """
        Delete an existing group using the ID
        """
        result = r.table("groups").get(group_id).delete().run(conn)

        if result["deleted"] == 1:
            return {"response": "Successfully deleted the group!"}, 200

        else:
            return {"response": "Error 404! The group wasn't found!"}, 404
