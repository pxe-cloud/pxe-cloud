#!/bin/sh

# Start serving the API with uWSGI (reading the IP and the port from the settings file (without logging to avoid displaying the passwords of the users)
uwsgi --socket $(cat settings.yml | shyaml get-value network.host_ip):$(cat settings.yml | shyaml get-value network.api_port) --protocol=http -w wsgi -L
