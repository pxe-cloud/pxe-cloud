#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask import Response
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators methods
from api.decorators.authentication_decorators import authorized
from api.decorators.rethinkdb_decorators import rethinkdb_connection

# Methods imports
from api.methods.strings_methods import normalize_string
from api.methods.menus_methods import generate_menu


# Organizations Script resource
class OrganizationsScript(Resource):

    # GET
    @authorized
    @rethinkdb_connection
    def get(self, username, conn):
        parser = reqparse.RequestParser()
        parser.add_argument("password", type=str, help="This is the password of the user")
        args = parser.parse_args()

        user = r.table("users").get(username).run(conn)

        if len(user["organizations"]) > 1:
            raw_menu = "item --gap -- ---- Organizations ----\n"
            entries_menu = ""

            for organization_id in user["organizations"]:
                organization = r.table("organizations").get(organization_id).run(conn)
                normalized_name = normalize_string(organization["name"])

                raw_menu += f"item {normalized_name} {organization['name']} -->\n"

                entries_menu += f":{normalized_name}\n"
                entries_menu += f"chain http://api.pxecloud.tk/boot/{username}/{organization_id}" + "?username=${username:uristring}&password=${password:uristring}\n"

            ipxe_script = generate_menu(username, args['password'], "Choose organization", raw_menu, entries_menu)

        else:
            ipxe_script = f"#!ipxe\nset username={username}\nset password={args['password']}\nchain http://api.pxecloud.tk/boot/{username}/{user['organizations'][0]}" + "?username=${username:uristring}&password=${password:uristring}\n"

        return Response(ipxe_script, mimetype="text/plain")
