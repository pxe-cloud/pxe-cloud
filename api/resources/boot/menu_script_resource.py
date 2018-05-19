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


# Menu Script resource
class MenuScript(Resource):

    # GET
    @authorized
    @rethinkdb_connection
    def get(self, username, organization_id, group_id, conn):
        parser = reqparse.RequestParser()
        parser.add_argument("password", type=str, help="This is the password of the user")
        args = parser.parse_args()

        menu_id = r.table("groups").get(group_id).run(conn)["menu_id"]
        menu = r.table("menus").get(menu_id).run(conn)

        api_settings = read_settings('api')
        protocol = api_settings['protocol']
        domain_name = api_settings['domain_name']

        raw_menu = ""
        entries_menu = ""

        for entry in sorted(menu["entries"], key=lambda item: item["position"]):
            if entry["type"] == "separator":
                raw_menu += f"item\nitem --gap -- ---- {entry['content']} ----\n"

            elif entry["type"] == "image":
                image = r.table("images").get(entry["image_id"]).run(conn)
                normalized_title = normalize_string(image["title"])

                raw_menu += f"item {normalized_title} {image['title']} -->\n"

                if image["type"] == "iso":
                    entries_menu += f":{normalized_title}\n"
                    entries_menu += f"kernel memdisk\n"
                    entries_menu += f"initrd {image['image_source']}\n"
                    entries_menu += f"imgargs memdisk iso raw {' '.join([arg for arg in image['boot_args']])}\n"

                elif image["type"] == "kernel_initrd":
                    entries_menu += f":{normalized_title}\n"

                    if "repository_url" in image:
                        entries_menu += f"kernel {image['kernel_source']} repo={image['repository_url']}\n"

                    else:
                        entries_menu += f"kernel {image['kernel_source']}\n"

                    entries_menu += f"initrd {image['image_source']}\n"

                entries_menu += "boot\n"

        ipxe_script = generate_menu(username, args["password"], menu["title"], raw_menu, entries_menu, menu["background"])
        print(ipxe_script)
        return Response(ipxe_script, mimetype="text/plain")
