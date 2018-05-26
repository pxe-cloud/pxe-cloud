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


# Close the DB connection
def close(conn):
    conn.close()
    del conn
    return True


# Create the needed tables
def setup():
    db_name = rethink_settings["db_name"]

    conn = connect()
    r.db_create(db_name).run(conn)
    r.db(db_name).table_create("users", primary_key="username").run(conn)
    r.db(db_name).table_create("users").run(conn)
    r.db(db_name).table_create("organizations").run(conn)
    r.db(db_name).table_create("groups").run(conn)
    r.db(db_name).table_create("menus").run(conn)
    r.db(db_name).table_create("images").run(conn)
    close(conn)
