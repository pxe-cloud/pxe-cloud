#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import pytest
import sys
import os

def os_move_to_project_root(initial_os_path):
    """
    Move to the root directory of the project using the `os` module
    """
    for index, directory in reversed(list(enumerate(initial_os_path.split("/")))):
        if directory == "tests":
            os.chdir("../../")
            return

        else:
            os.chdir("../")


def sys_move_to_project_root(initial_sys_path):
    """
    Move to the root directory of the project using the `sys` module
    """
    for index, directory in reversed(list(enumerate(initial_sys_path.split("/")))):
        if directory == "tests":
            sys.path[0] = "/".join(sys.path[0].split("/")[:-2])
            return

        else:
            sys.path[0] = "/".join(sys.path[0].split("/")[:-1])

@pytest.fixture()
def move_to_project_root():
    """
    Change the running execution environment to the root of the project
    """
    initial_os_path = os.getcwd()
    initial_sys_path = sys.path[0]

    # Move to the project root
    os_move_to_project_root(initial_os_path)
    sys_move_to_project_root(initial_sys_path)

    # Execute the test
    yield

    # Return to the original path
    os.chdir(initial_os_path)
    sys.path[0] = initial_sys_path

