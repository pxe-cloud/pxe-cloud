#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Methods imports
from api.methods.files_methods import read_settings
from api.methods.rethinkdb_methods import connect

# Organization resource
class Organization(Resource):

    # GET
    def get(self, organization_id):
        """
        Get a specific organization using an id
        """
        rethink_settings = read_settings("rethinkdb")
        connect(r)
        organization = r.db(rethink_settings["db_name"]).table("organizations").get(organization_id).run()

        if organization:
            return {"response": organization}, 200

        else:
            return {"response": "Error 404! The organization wasn't found!"}, 404

    # PUT
    def put(self, organization_id):
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

        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("organizations").get(organization_id).update(to_update).run()

        if result["replaced"] == 1:
            return {"response": "Successfully updated the organization!"}, 200

        elif result["unchanged"] == 1:
            return {"response": "Error 204! Please make changes!"}, 204

        else:
            return {"response": "Error 404! Organization not found!"}, 404

    # DELETE
    def delete(self, organization_id):
        """
        Delete an existing organization using the ID
        """
        rethink_settings = read_settings("rethinkdb")
        connect(r)
        result = r.db(rethink_settings["db_name"]).table("organizations").get(organization_id).delete().run()

        if result["deleted"] == 1:
            return {"response": "Successfully deleted the organization!"}, 200

        else:
            return {"response": "Error 404! The organization wasn't found!"}, 404
