#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Boot Arg resource
class BootArg(Resource):

    # DELETE
    @rethinkdb_connection
    def delete(self, image_id, boot_arg, conn):
        """
        Delete an existing boot arg
        """
        image = r.table("images").get(image_id)
        boot_args = dict(r.table("images").get(image_id).run(conn))["boot_args"]
        print(boot_arg, boot_args)

        try:
            del boot_args[boot_arg]

        except KeyError:
            return {"response": "Error 404! Boot argument not found"}, 404

        result = image.update({"boot_args": boot_args}).run(conn)
        print(boot_args)
        print(result)

        if result["replaced"] == 1:
            return {"response": "Successfully deleted the boot argument!"}, 200

        else:
            return {"response": "Error 500! Internal server error!"}, 500
