#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# User Group resource
class UserGroup(Resource):

    # POST
    @rethinkdb_connection
    def post(self, username, group_id, conn):
        """
        Add an existing user to an existing group
        """
        try:
            r.table("users").get(username).run(conn)["groups"].index(group_id)

        except ValueError:
            result = r.table("users").get(username).update({"groups": r.row["groups"].append(group_id)}).run(conn)

            if result["replaced"] == 1:
                return {"response": "Successfully added the user to the group!"}, 200

        else:
            return {"response": "Error 409! The user is already in the group!"}, 409

    # DELETE
    @rethinkdb_connection
    def delete(self, username, group_id, conn):
        """
        Remove an existing user from an existing group
        """
        groups = r.table("users").get(username).run(conn)["groups"]

        try:
            position_group_to_delete = groups.index(group_id)

        except ValueError:
            return {"response": "Error 404! The user isn't in the group!"}, 404

        result = r.table("users").get(username).update({
            "groups": r.row["groups"].delete_at(position_group_to_delete)
        }).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully removed the user form the group!"}, 200

        else:
            return {"response": "Error 500! Internal server error!"}, 500
