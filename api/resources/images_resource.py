#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Images resource
class Images(Resource):

    # GET
    @rethinkdb_connection
    def get(self, conn):
        """
        Return all the existing images
        """
        images = r.table("images").run(conn)

        return {"response": [menu for menu in images]}, 200

    # POST
    @rethinkdb_connection
    def post(self, conn):
        """
        Create a new image
        """
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, help="This is the title of the image")
        parser.add_argument("type", type=str, help="This is the type of the image (iso, kernel_initrd)")
        parser.add_argument("image_source", type=str, help="This is the url (the source) of the image (iso, initramfs)")
        parser.add_argument("kernel_source", type=str, help="This is the url (the source) of the kernel")
        parser.add_argument("repository_url", type=str, help="This is the url of the repository (needed by Red Hat installers)")
        parser.add_argument("boot_args", type=str, help="Aditional parameters passsed to the isos when booting")
        args = parser.parse_args()

        for key, value in args.items():
            if not value:
                args[key] = ""

        new_image = dict()
        new_image["title"] = args["title"]
        new_image["type"] = args["type"]
        new_image["image_source"] = args["image_source"]
        new_image["repository_url"] = args["repository_url"]
        new_image["kernel_source"] = args["kernel_source"]
        new_image["boot_args"] = args["boot_args"]

        result = r.table("images").insert([new_image]).run(conn)

        if result["inserted"] == 1:
            return {"response": "Successfully created the image!"}, 201, {"Location": f"/image/{result['generated_keys'][0]}"}

        else:
            return {"response": "Error 500! Internal server error!"}, 500
