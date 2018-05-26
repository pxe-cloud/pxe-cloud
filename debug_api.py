#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from api.app import app

# Methods imports
from api.methods.files_methods import read_settings

# Run the app
if __name__ == "__main__":
    network_settings = read_settings("network")
    app.run(debug=True, host=network_settings["host_ip"], port=network_settings["api_port"])
