#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource
from flask import send_from_directory
import os

# Decorators imports
from api.decorators.authentication_decorators import authorized

# Methods imports
from api.methods.files_methods import read_settings

# Return image resource
class ReturnImage(Resource):

    # GET
    @authorized
    def get(self, username, organization_id, group_id, image_id):
        images_directory = read_settings("storage")["path"]

        if image_id == "memdisk":
            return send_from_directory(os.path.abspath(images_directory), "memdisk")

        return {"response": "Error 404! Image not found!"}, 404