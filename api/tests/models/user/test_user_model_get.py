#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import pytest

class TestUserModelGet:
    """
    Test all the possible responses and errors of the get() method from the User model
    """
    def test_get_non_string(self, import_module, user):
        """
        Try getting an user without passing an string
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(TypeError) as excinfo:
            User().get({"username": user["username"]})

        assert "Username needs to be a string" in str(excinfo.value)


    def test_get_not_found(self, import_module, user):
        """
        Try getting a nonexistent user
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(KeyError) as excinfo:
            User().get(user["username"] + "idontexist")

        assert "The user wasn't found in the DB!" in str(excinfo.value)

    def test_get_return_user(self, import_module, user):
        """
        Try getting an
        """
        User = import_module(path="api.models.user", module="User")

        user = User().get(user["username"], return_user=True)

        assert isinstance(user, dict) and \
               all(key in user for key in ["username", "password", "email", "organizations", "groups"])

    def test_get_return_self(self, import_module, user):
        User = import_module(path="api.models.user", module="User")

        user = User().get(user["username"])

        # Check if what was returned was an instance of the User class
        assert isinstance(user, User)
