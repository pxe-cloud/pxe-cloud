#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import os
import yaml


# Read the settings
def read_settings(key=None):
    with open(os.path.abspath("../settings.yml")) as file:
        settings = yaml.safe_load(file)

    if key:
        return settings[key]

    else:
        return settings
