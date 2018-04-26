#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r

# Methods imports
from api.methods.files_methods import read_settings

# Read the settings related to RethinkDB
rethink_settings = read_settings("rethinkdb")


# Connect to the DB
def connect(db):
    db.connect(rethink_settings["host"], rethink_settings["port"]).repl()


# Create the needed tables
def setup():
    connect(r)
    r.db_create(rethink_settings["db_name"]).run()
    r.db(rethink_settings["db_name"]).table_create("users").run()
    r.db(rethink_settings["db_name"]).table_create("organizations").run()
    r.db(rethink_settings["db_name"]).table_create("groups").run()
    r.db(rethink_settings["db_name"]).table_create("menus").run()
    r.db(rethink_settings["db_name"]).table_create("images").run()


