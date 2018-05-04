#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask import Response
from flask_restful import Resource, reqparse

# Decorators imports
from api.decorators.authentication_decorators import authorized

# Methods imports
from api.methods.files_methods import read_settings


# Auth resource
class BootAuth(Resource):

    # GET
    @authorized(f"""#!ipxe
set username
set password
login
chain {read_settings('api')['protocol']}://{read_settings('api')['domain_name']}/boot""" + """?username=${username:uristring}&password=${password:uristring}""")
    def get(self):
        """
        Try to authenticate an user. If the authentication is successful, it returns a user menu. If not, it returns a login menu
        """
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="This is the username of the user")
        parser.add_argument("password", type=str, help="This is the password of the user")
        args = parser.parse_args()

        return_script = "#!ipxe\n"
        return_script += f"set username {args['username']}\n"
        return_script += f"set password {args['password']}\n"
        return_script += f"chain {read_settings('api')['protocol']}://{read_settings('api')['domain_name']}/boot/" + "${username:uristring}?username=${username:uristring}&password=${password:uristring}\n"

        return Response(return_script, mimetype="text/plain")
