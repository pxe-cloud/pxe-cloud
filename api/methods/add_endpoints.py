#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from api.methods.files_methods import read_settings

# Resources imports


# Add all the endpoints to the API
def add_endpoints(api):
    root = read_settings("api")["base_url"]
