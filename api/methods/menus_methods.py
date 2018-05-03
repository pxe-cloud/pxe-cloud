#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection

# Methods imports
from api.methods.strings_methods import normalize_string


# Generate a menu
def generate_menu(username, password, menu_title, items_to_add, entries_to_add, background_url=None):
    raw_menu = "#!ipxe\n"
    entries_menu = ""

    raw_menu += f"set username {username}\n"
    raw_menu += f"set password {password}\n"

    if background_url:
        raw_menu += f"console --x 1280 --y 720 --picture {background_url} --left 50 --right 50 --top 30 --bottom 30\n"

    raw_menu += f"menu {menu_title}\n"

    raw_menu += items_to_add
    entries_menu += entries_to_add

    raw_menu += "item\n"
    raw_menu += "item --gap -- ---- Actions ----\n"
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
