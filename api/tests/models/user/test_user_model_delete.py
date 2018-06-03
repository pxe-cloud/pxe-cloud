#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TestUserModelDelete:
    """
    Test all the possible responses and errors of the delete() method from the User model
    """
    def test_delete(self, import_module, user):
        """
        Delete a specific user from the DB
        """
        User = import_module(path="api.models.user", module="User")

        assert User().get(user["username"]).delete()
