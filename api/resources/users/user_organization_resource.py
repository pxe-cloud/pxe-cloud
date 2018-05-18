#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# User Organization resource
class UserOrganization(Resource):

    # POST
    @rethinkdb_connection
    def post(self, username, organization_id, conn):
        """
        Add an existing user to an existing organization
        """
        try:
            r.table("users").get(username).run(conn)["organizations"].index(organization_id)

        except ValueError:
            result = r.table("users").get(username).update({"organizations": r.row["organizations"].append(organization_id)}).run(conn)

            if result["replaced"] == 1:
                return {"response": "Successfully added the user to the organization!"}, 200

        else:
            return {"response": "Error 409! The user is already in the organization!"}, 409

    # DELETE
    @rethinkdb_connection
    def delete(self, username, organization_id, conn):
        """
        Remove an existing user from an existing organization
        """
        organizations = r.table("users").get(username).run(conn)["organizations"]

        try:
            position_organization_to_delete = organizations.index(organization_id)

        except ValueError:
            return {"response": "Error 404! The user isn't in the organization!"}, 404

        result = r.table("users").get(username).update({
            "organizations": r.row["organizations"].delete_at(position_organization_to_delete)
        }).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully removed the user from the organization!"}, 200

        else:
            return {"response": "Error 500! Internal server error!"}, 500