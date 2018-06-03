#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import pytest

class TestUserModelCreate:
    """
    Test all the possible responses and errors of the create() method from the User model
    """
    def test_clear_table(self, import_module):
        """
        Clear the table before running all the tests
        """
        clear_table = import_module(path="api.methods.rethinkdb_methods", module="clear_table")
        clear_table("users")

    def test_create_username_non_string(self, import_module, user):
        """
        Try creating an user without passing an string in the username
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(TypeError) as excinfo:
            User().create([user["username"]], user["password"], user["email"])

        assert "Username needs to be a string!" in str(excinfo.value)

    def test_create_password_non_string(self, import_module, user):
        """
        Try creating an user without passing an string in the password
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(TypeError) as excinfo:
            User().create(user["username"], [user["password"]], user["email"])

        assert "Password needs to be a string!" in str(excinfo.value)

    def test_create_email_non_string(self, import_module, user):
        """
        Try creating an user without passing an string in the email
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(TypeError) as excinfo:
            User().create(user["username"], user["password"], [user["email"]])

        assert "Email needs to be a string!" in str(excinfo.value)

    def test_create(self, import_module, user):
        """
        Create a new user
        """
        User = import_module(path="api.models.user", module="User")

        assert User().create(user["username"], user["password"], user["email"])

    def test_create_email_already_exists(self, import_module, user):
        """
        Try creating an user with an username that already exists
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(ValueError) as excinfo:
            User().create(user["username"], user["password"], user["email"])

        assert "There's already an user with this username!" in str(excinfo.value)
