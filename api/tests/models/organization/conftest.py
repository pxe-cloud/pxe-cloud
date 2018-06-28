#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import pytest

organizations = [
    {
        "name": "Escola del Treball",
        "description": None
    },
    {
        "name": "PXE Cloud",
        "description": "PXE Cloud is the organization of the PXE Cloud project"
    }
]


@pytest.fixture(scope="class", params=organizations)
def organization(request):
    """
    Acts as the parametrize decorator
    """
    return request.param
