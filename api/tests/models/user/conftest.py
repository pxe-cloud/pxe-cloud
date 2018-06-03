#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import pytest

users = [
    {
        "username": "nefix",
        "password": "1234",
        "email": "nefix@pxecloud.tk",
        "new_password": "1357",
        "new_email": None
    }, {
        "username": "jorge",
        "password": "4321",
        "email": "jorge@pxecloud.tk",
        "new_password": None,
        "new_email": "jorge@pxecloud.io"
    }
]

@pytest.fixture(scope="class", params=users)
def user(request):
    """
    Acts as the parametrize decorator
    """
    return request.param
