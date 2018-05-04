#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Image resource
class Image(Resource):

    # GET
    @rethinkdb_connection
    def get(self, image_id, conn):
        """
        Get a specific image using the id
        """
        image = r.table("images").get(image_id).run(conn)

        if image:
            return {"response": image}, 200

        else:
            return {"response": "Error 404! The menu wasn't found"}, 404

    # PUT
    @rethinkdb_connection
    def put(self, image_id, conn):
        """
        Update an existing image using the id
        """
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, help="This is the title of the image")
        parser.add_argument("type", type=str, help="This is the type of the image (iso, kernel_initrd)")
        parser.add_argument("image_source", type=str, help="This is the url (the source) of the image (iso, initramfs)")
        parser.add_argument("kernel_source", type=str, help="This is the url (the source) of the kernel")
        parser.add_argument("repository_url", type=str, help="This is the url of the repository (needed by Red Hat installers)")
        parser.add_argument("boot_args", type=str, help="Additional parameters passed to the isos when booting")
        args = parser.parse_args()

        # Update only the parameters that are passed
        to_update = {}
        for arg, value in args.items():
            if value:
                to_update[arg] = value

        result = r.table("images").get(image_id).update(to_update).run(conn)

        if result["replaced"] == 1:
            return {"response": "Successfully updated the image!"}, 200

        elif result["unchanged"] == 1:
            return {"response": "Error 400! Please make some changes!"}, 400

        else:
            return {"response": "Error 404! The image wasn't found!"}, 404

    # DELETE
    @rethinkdb_connection
    def delete(self, image_id, conn):
        """
        Delete an existing image using the ID
        """
        result = r.table("images").get(image_id).delete().run(conn)

        if result["deleted"] == 1:
            return {"response": "Successfully deleted the image!"}, 200

        else:
            return {"response": "Error 404! The image wasn't found!"}, 404
