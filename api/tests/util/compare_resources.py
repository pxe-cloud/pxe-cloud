#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Compare:
    """
    Compare two resources
    """
    def user(self, user_1, user_2, params_to_ignore=[]):
        params = ["username", "password", "email", "organizations", "groups"]
        for param in params_to_ignore:
            try:
                params.remove(param)

            except ValueError:
                print("The parameter {} doesn't exist!".format(param))

        conditions = []
        for param in params:
            conditions.append((user_1[param] == user_2[param]))

        return all(conditions)
