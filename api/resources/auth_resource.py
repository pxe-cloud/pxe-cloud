#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask import Response
from flask_restful import Resource

# Decorators imports
from api.decorators.authentication_decorators import authorized


# Auth resource
class Auth(Resource):

    # GET
    @authorized("""#!ipxe
set username
set password
login
chain http://api.pxecloud.tk/auth?username=${username:uristring}&password=${password:uristring}""")
    def get(self):
        """
        Try to authenticate an user. If the authentication is successful, it returns a user menu. If not, it returns a login menu
        """
        return Response("""#!ipxe
set username nefix
set password 1234
chain http://api.pxecloud.tk/boot/${username:uristring}?username=${username:uristring}&password=${password:uristring}""", mimetype="text/plain")
