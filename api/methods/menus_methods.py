#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r

# Decorators imports
from api.decorators.authentication_decorators import authorized
from api.decorators.rethinkdb_decorators import rethinkdb_connection

# Methods imports
from api.methods.strings_methods import normalize_string


# Generate a menu
@authorized
@rethinkdb_connection
def generate_menu(menu_id, username, password, conn):
    menu = r.table("menus").get(menu_id).run(conn)

    raw_menu = "#!ipxe\n"
    entries_menu = ""

    if menu["background"]:
        raw_menu += f"console --x 1024 --y 576 --picture {menu['background']} --left 50 --right 50 --top 30 --bottom 30"

    raw_menu += f"set username={username}\n"
    raw_menu += f"set password={password}\n"

    raw_menu += f"menu {menu['title']}\n"

    for entry in sorted(menu["entries"], key=lambda item: item["position"]):
        if entry["type"] == "separator":
            raw_menu += f"item --gap {entry['content']}\n"

        # TODO: Actions

        elif entry["type"] == "image":
            normalized_title = normalize_string(entry['title'])
            raw_menu += f"item {normalized_title} {entry['title']} -->\n"

            if entry["image_type"] == "iso":
                entries_menu += f":{normalized_title}\n"
                entries_menu += f"kernel #TODO: # || read void\n"
                entries_menu += f"initrd {entry['image_source']} || read void\n"
                entries_menu += f"imgargs memdisk iso raw {' '.join([arg for arg in entry['boot_args']])}|| read void\n"
                entries_menu += "boot || read void\n"

            if entry["image_type"] == "kernel_initrd":
                entries_menu += f":{normalized_title}\n"

                if entry["repo"]:
                    entries_menu += f"kernel {entry['kernel']} repo={entry['repo']} || read void\n"

                else:
                    entries_menu += f"kernel {entry['kernel']} || read void\n"

                entries_menu += f"initrd {entry['initrd']} || read void\n"
                entries_menu += "boot || read void\n"

    raw_menu += "item --gap Actions:\n"
    raw_menu += "item boot_from_disk Boot from disk -->\n"
    raw_menu += "item reboot Reboot -->\n"
    raw_menu += "item shutdown Shutdown -->\n"
    entries_menu += ":boot_from_disk\n"
    entries_menu += "sanboot --no-describe --drive 0x80\n"
    entries_menu += ":reboot\n"
    entries_menu += "reboot\n"
    entries_menu += ":shutdown\n"
    entries_menu += "poweroff\n"

    raw_menu += "choose target && goto ${target}\n"
    raw_menu += entries_menu

    return raw_menu
