#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Boot Arg resource
class BootArg(Resource):

    # GET
    @rethinkdb_connection
    def get(self, image_id, boot_arg, conn):
        """
        Get a specific boot arg
        """
        boot_args = r.table("images").get(image_id).run(conn)["boot_args"]

        if boot_args or boot_args == []:
            try:
                return {"response": {boot_arg: boot_args[boot_arg]}}, 200

            except KeyError:
                return {"response": "Error 404! Boot argument not found"}, 404

        else:
            return {"response": "Error 404! Image not found!"}, 404

    # PUT
    @rethinkdb_connection
    def put(self, image_id, boot_arg, conn):
        """
        Update an existing boot arg
        """
        parser = reqparse.RequestParser()
        parser.add_argument("value", required=True, type=str, help="The value of the boot argument")
        args = parser.parse_args()

        boot_args = r.table("images").get(image_id).run(conn)["boot_args"]

        if boot_args or boot_args == []:
            try:
                boot_args[boot_arg]

            except KeyError:
                return {"response": "Error 404! Boot argument not found"}, 404

            else:
                if not args["value"]:
                    args["value"] = None

                boot_args[boot_arg] = args["value"]

                result = r.table("images").get(image_id).update({"boot_args": boot_args}).run(conn)

                if result["replaced"] == 1:
                    return {"response": "Successfully updated the boot argument!"}, 201

                elif result["unchanged"] == 1:
                    return {"response": "Error 400! Please make changes!"}, 400

                else:
                    return {"response": "Error 500! Internal server error!"}, 500

    # DELETE
    @rethinkdb_connection
    def delete(self, image_id, boot_arg, conn):
        """
        Delete an existing boot arg
        """
        boot_args = r.table("images").get(image_id).run(conn)["boot_args"]

        if boot_args or boot_args == []:
            try:
                boot_args[boot_arg]

            except KeyError:
                return {"response": "Error 404! Boot argument not found"}, 404

            else:
                result = r.table("images").get(image_id).replace(r.row.without({"boot_args": {boot_arg}})).run(conn)

                if result["replaced"] == 1:
                    return {"response": "Successfully deleted the boot argument!"}, 200

                else:
                    return {"response": "Error 500! Internal server error!"}, 500

        else:
            return {"response": "Error 404! Image not found!"}, 404
