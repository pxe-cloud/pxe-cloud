#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask import Response
from flask_restful import reqparse

# Decorators methods
from api.decorators.decorators_decorators import optional_args_decorator

# Methods imports
from api.methods.encryption_methods import check_auth


@optional_args_decorator
def authorized(f, return_menu=None):
    # TODO: Check if the user has permissions to do the stuff is doing
    def wrapper(*args, **kwargs):
        # Parse the arguments passed
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="This is the username of the user")
        parser.add_argument("password", type=str, help="This is the password of the user")
        user_credentials = parser.parse_args()

        if check_auth(user_credentials):
            return f(*args, **kwargs)

        else:
            if not return_menu:
                return {"response": "Error 401! Your login information is incorrect!"}, 401

            else:
                # TODO: Change this return to an actual menu found by ID
                return Response(return_menu, mimetype="text/html")
    return wrapper
