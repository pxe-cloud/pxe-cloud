#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Organization resource
class Organization(Resource):

    # GET
    @rethinkdb_connection
    def get(self, organization_id, conn):
        """
        Get a specific organization using an id
        """
        organization = r.table("organizations").get(organization_id).run(conn)

        if organization:
            return {"response": organization}, 200

        else:
            return {"response": "Error 404! The organization wasn't found!"}, 404

    # PUT
    @rethinkdb_connection
    def put(self, organization_id, conn):
        """
        Update an existing organization using the ID
        """
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="This is the name of the organization")
        parser.add_argument("description", type=str, help="This is a small description of the organization")
        args = parser.parse_args()

        # Update only the parameters that are passed
        to_update = {}
        for arg, value in args.items():
            if value:
                to_update[arg] = value

        result = r.table("organizations").get(organization_id).update(to_update).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully updated the organization!"}, 200

        elif result["unchanged"] == 1:
            return {"response": "Error 400! Please make some changes!"}, 400

        else:
            return {"response": "Error 404! Organization not found!"}, 404

    # DELETE
    @rethinkdb_connection
    def delete(self, organization_id, conn):
        """
        Delete an existing organization using the ID
        """
        result = r.table("organizations").get(organization_id).delete().run(conn)

        if result["deleted"] == 1:
            return {"response": "Successfully deleted the organization!"}, 200

        else:
            return {"response": "Error 404! The organization wasn't found!"}, 404
