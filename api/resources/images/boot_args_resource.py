#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Boot Args resource
class BootArgs(Resource):

    # GET
    @rethinkdb_connection
    def get(self, image_id, conn):
        """
        Return all the boot args of an image
        """
        boot_args = r.table("images").get(image_id).run(conn)["boot_args"]

        return {"response": boot_args}


    # POST
    @rethinkdb_connection
    def post(self, image_id, conn):
        """
        Adds a new boot arg of an image
        """
        parser = reqparse.RequestParser()
        parser.add_argument("key", type=str, help="The key of the boot argument")
        parser.add_argument("value", type=str, help="The value of the boot argument")
        args = parser.parse_args()

        image = r.table("images").get(image_id)
        boot_args = dict(r.table("images").get(image_id).run(conn))["boot_args"]
        boot_args[args["key"]] = args["value"]
        result = image.update({"boot_args": boot_args}).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully added the boot argument!"}, 201

        elif result["unchanged"] == 1:
            return {"response": "Error 400! Please make changes!"}, 400

        else:
            return {"response": "Error 500! Internal server error!"}, 500
