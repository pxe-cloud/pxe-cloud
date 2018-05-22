#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Organization Group resource
class OrganizationGroup(Resource):

    # POST
    @rethinkdb_connection
    def post(self, organization_id, group_id, conn):
        """
        Add an existing group to an existing organization
        """
        try:
            r.table("organizations").get(organization_id).run(conn)["groups"].index(group_id)

        except ValueError:
            result = r.table("organizations").get(organization_id).update({"groups": r.row["groups"].append(group_id)}).run(conn)

            if result["replaced"] == 1:
                return {"response": "Successfully added the group to the organization"}, 200

            else:
                return {"response": "Error 500! Internal server error!"}, 500

        else:
            return {"response": "Error 409! The group is already in the organization!"}, 409

    # DELETE
    @rethinkdb_connection
    def delete(self, organization_id, group_id, conn):
        """
        Remove an existing group from an existing organization
        """
        groups = r.table("organizations").get(organization_id).run(conn)["groups"]

        try:
            position_group_to_delete = groups.index(group_id)

        except ValueError:
            return {"response": "Error 404! The group isn't in the organization!"}, 404

        result = r.table("organizations").get(organization_id).update({
            "groups": r.row["groups"].delete_at(position_group_to_delete)
        }).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully removed the group from the organization!"}, 200

        else:
            return {"response": "Error 500! Internal server error!"}, 500