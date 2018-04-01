#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import sys
from urllib import request
import subprocess
import argparse
import yaml


# Check Python version and if pip is installed
def check_python_and_pip():
    if not sys.version_info >= (3, 6):
        print("Python 3.6 or newer is required to use PXE Cloud. Please, install it.")
        sys.exit(1)

    else:
        # Try using Pip, if it's not available, ask if the user wants to install it
        try:
            import pip

        except ImportError:
            response = input("Pip isn't installed, do you want to install it? [Y/n]: ")

            if response == "Y" or response == "y" or response == "":
                request.urlretrieve("https://bootstrap.pypa.io/get-pip.py")
                command = f"sudo python-{sys.version_info[0]}.{sys.version_info[1]} get-pip.py"
                subprocess.run(command.split(" "))

                import pip

            else:
                print("You need pip in order to use PXE Cloud. Please, install it.")
                sys.exit(1)


# Install dependencies
def install_dependencies():
    create_venv_command = f"python{sys.version_info[0]}.{sys.version_info[1]} -m venv venv"
    install_dependencies_command = "./venv/bin/pip install -r requirements.txt"
    subprocess.run(create_venv_command.split(" "))
    subprocess.run(install_dependencies_command.split(" "))


# Create the files
def generate_files():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", "-a", help="Ip adress of the server")
    parser.add_argument("--port", "-p", help="Port of the API server")
    parser.add_argument("--base-url", "-b", help="Base url of the API (http://localhost:5000/<base-url>/<endpoints>)")
    args = parser.parse_args()
    response = {}

    if args.address:
        response["host_ip"] = args.address
    else:
        response["host_ip"] = "0.0.0.0"

    if args.port:
        response["api_port"] = args.port
    else:
        response["api_port"] = "0.0.0.0"

    if args.base_url:
        response["base_url"] = args.base_url
    else:
        response["base_url"] = "/api"

    with open("../settings.yml", "w+") as f:
        to_write = {"network": {"host_ip": response["host_ip"], "api_port": response["api_port"]}, "api": {"base_url": response["base_url"]}}
        yaml.dump(to_write, f)


# Run the functions
if __name__ == "__main__":
    check_python_and_pip()
    install_dependencies()
    generate_files()
    print(f"Installation successful! To run PXE Cloud, simply execute 'python{sys.version_info[0]}.{sys.version_info[1]} run_api.py' (remember to activate use venv)")
