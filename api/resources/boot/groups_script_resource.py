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
from api.methods.files_methods import read_settings


# Groups Script resource
class GroupsScript(Resource):

    # GET
    @authorized
    @rethinkdb_connection
    def get(self, username, organization_id, conn):
        parser = reqparse.RequestParser()
        parser.add_argument("password", type=str, help="This is the password of the user")
        args = parser.parse_args()

        user = r.table("users").get(username).run(conn)
        organization = r.table("organizations").get(organization_id).run(conn)

        api_settings = read_settings('api')
        protocol = api_settings['protocol']
        domain_name = api_settings['domain_name']

        if len(user["groups"]) > 1:
            raw_menu = "item --gap -- ---- Groups ----\n"
            entries_menu = ""

            organization_user_groups = 0

            for group_id in user["groups"]:
                if group_id in organization["groups"]:
                    group = r.table("groups").get(group_id).run(conn)
                    normalized_name = normalize_string(group["name"])

                    organization_user_groups += 1
                    organization_user_group_id = group_id

                    raw_menu += f"item {normalized_name} {group['name']} -->\n"

                    entries_menu += f":{normalized_name}\n"
                    entries_menu += f"chain {protocol}://{domain_name}/boot/{username}/{organization_id}/{group_id}" + "?username=${username:uristring}&password=${password:uristring}\n"

            if organization_user_groups > 1:
                ipxe_script = generate_menu(username, args["password"], "Choose group", raw_menu, entries_menu)

            else:
                ipxe_script = f"#!ipxe\nset username={username}\nset password={args['password']}\nchain {protocol}://{domain_name}/boot/{username}/{organization_id}/{group_id}" + "?username=${username:uristring}&password=${password:uristring}\n"

        else:
            ipxe_script = f"#!ipxe\nset username={username}\nset password={args['password']}\nchain {protocol}://{domain_name}/boot/{username}/{organization_id}/{user['groups'][0]}" + "?username=${username:uristring}&password=${password:uristring}\n"

        return Response(ipxe_script, mimetype="text/plain")
