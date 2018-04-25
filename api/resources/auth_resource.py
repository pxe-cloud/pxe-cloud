#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask import Response
from flask_restful import Resource, reqparse
from api.methods.authentication_methods import check_auth


# Auth resource
class Auth(Resource):

    # GET
    def get(self):
        """
        Try to authenticate an user. If the authentication is successful, it returns a user menu. If not, it returns a login menu
        """
        # Parse the arguments passed
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="This is the username of the user")
        parser.add_argument("password", type=str, help="This is the password of the user")
        args = parser.parse_args()

        if check_auth(args):
            return Response("""#!ipxe
echo Successfully logged in!""")

        else:
            return Response("""#!ipxe
login
chain http://api.pxecloud.tk/auth?username=${username:uristring}&password=${password:uristring}""", mimetype="text/html")
