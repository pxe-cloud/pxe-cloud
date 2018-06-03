#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import pytest

class TestUserModelUpdate:
    """
    Test all the possible responses and errors of the update() method from the User model
    """
    def test_update_new_password_non_string(self, import_module, user):
        """
        Try updating an user without passing a string in the password
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(TypeError) as excinfo:
            User().get(user["username"]).update(new_password=[user["new_password"]], new_email=user["new_email"])

        assert "Password needs to be a string!" in str(excinfo.value)

    def test_update_new_emai_non_string(self, import_module, user):
        """
        Try updating an user without passing a string in the email
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(TypeError) as excinfo:
            User().get(user["username"]).update(new_password=user["new_password"], new_email=[user["new_email"]])

        assert "Email needs to be a string!" in str(excinfo.value)


    def test_update_empty_values(self, import_module, user):
        """
        Try updating an user without passing any value
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(ValueError) as excinfo:
            User().get(user["username"]).update()

        assert "You need to make some changes!" in str(excinfo.value)

    def test_update_same_password(self, import_module, user):
        """
        Try updating an user without changing the password
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(ValueError) as excinfo:
            User().get(user["username"]).update(new_password=user["password"], new_email=user["new_email"])

        assert "You need to provide a different password in order to update it!" in str(excinfo.value)

    def test_update_same_email(self, import_module, user):
        """
        Try updating an user without changing the email address
        """
        User = import_module(path="api.models.user", module="User")

        with pytest.raises(ValueError) as excinfo:
            User().get(user["username"]).update(new_password=user["new_password"], new_email=user["email"])

        assert "You need to provide a different email in order to update it!" in str(excinfo.value)

    def test_update(self, import_module, user):
        """
        Update an user
        """
        User = import_module(path="api.models.user", module="User")

        assert User().get(user["username"]).update(new_password=user["new_password"], new_email=user["new_email"])
