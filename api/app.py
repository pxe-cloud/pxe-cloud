#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# Methods imports
from api.methods.add_endpoints import add_endpoints
from api.methods.files_methods import read_settings

# App initialization
app = Flask(__name__)
CORS(app)
api = Api(app)


# Add endpoints
add_endpoints(api)

# Run the app
network_settings = read_settings("network")
app.run(port=network_settings["api_port"], debug=True, host=network_settings["host_ip"])
