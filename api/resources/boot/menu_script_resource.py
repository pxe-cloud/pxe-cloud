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


# Menu Script resource
class MenuScript(Resource):

    # GET
    @authorized
    @rethinkdb_connection
    def get(self, username, organization_id, group_id, conn):
        parser = reqparse.RequestParser()
        parser.add_argument("password", type=str, help="This is the password of the user")
        args = parser.parse_args()

        menu_id = r.table("groups").get(group_id).run(conn)["menu"]
        menu = r.table("menus").get(menu_id).run(conn)

        raw_menu = ""
        entries_menu = ""

        for entry in sorted(menu["entries"], key=lambda item: item["position"]):
            if entry["type"] == "separator":
                raw_menu += f"item\nitem --gap {entry['content']}\n"

            elif entry["type"] == "image":
                normalized_title = normalize_string(entry['title'])
                raw_menu += f"item {normalized_title} {entry['title']} -->\n"

                if entry["image_type"] == "iso":
                    entries_menu += f":{normalized_title}\n"
                    entries_menu += f"kernel #TODO: #\n"
                    entries_menu += f"initrd {entry['image_source']}\n"
                    entries_menu += f"imgargs memdisk iso raw {' '.join([arg for arg in entry['boot_args']])}|| read void\n"

                if entry["image_type"] == "kernel_initrd":
                    entries_menu += f":{normalized_title}\n"

                    if "repo" in entry:
                        entries_menu += f"kernel {entry['kernel']} repo={entry['repo']}\n"

                    else:
                        entries_menu += f"kernel {entry['kernel']}\n"

                    entries_menu += f"initrd {entry['initrd']}\n"
                entries_menu += "boot\n"

        ipxe_script = generate_menu(username, args["password"], menu["title"], raw_menu, entries_menu, menu["background"])
        return Response(ipxe_script, mimetype="text/plain")
