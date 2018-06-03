#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Compare:
    """
    Compare two models
    """

    def users(self, user1, user2, params_to_ignore=()):
        """
        Compare two given users. Some parameters can be ignored
        """
        params = ["username", "password", "email", "organizations", "groups"]
        for param_to_ignore in params_to_ignore:
            if param_to_ignore in params:
                params.remove(param_to_ignore)

        compared_params = []
        for param in params:
            compared_params.append((user1[param] == user2[param]))

        print(compared_params)

        if all(compared_params):
            return True

        else:
            return False
