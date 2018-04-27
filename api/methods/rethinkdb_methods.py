#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r

# Methods imports
from api.methods.files_methods import read_settings

# Read the settings related to RethinkDB
rethink_settings = read_settings("rethinkdb")


# Connect to the DB
def connect():
    # Read the DB settings
    rethinkdb_settings = read_settings("rethinkdb")

    # Connect to the DB
    conn = r.connect(rethinkdb_settings["host"], rethinkdb_settings["port"], rethinkdb_settings["db_name"])
    return conn


def close(conn):
    conn.close()
    del conn
    return True


# Create the needed tables
def setup():
    connect(r)
    r.db_create(rethink_settings["db_name"]).run()
    # TODO: Change the PK
    r.db(rethink_settings["db_name"]).table_create("users").run()
    r.db(rethink_settings["db_name"]).table_create("organizations").run()
    r.db(rethink_settings["db_name"]).table_create("groups").run()
    r.db(rethink_settings["db_name"]).table_create("menus").run()
    r.db(rethink_settings["db_name"]).table_create("images").run()


