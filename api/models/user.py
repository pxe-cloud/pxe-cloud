#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection

# Methods imports
from api.methods.encryption_methods import encrypt_password

class User:
    """
    User model. This class should have all the operations related with the users
    """

    @rethinkdb_connection
    def get(self, username, conn, return_user=False):
        """
        Retrieve a specific user from the DB using the username
        """
        if not isinstance(username, str):
            raise TypeError("Username needs to be a string!")

        else:
            db_user = r.table("users").get(username).run(conn)
            if not db_user:
                raise KeyError("The user wasn't found in the DB!")

            else:
                self.username = db_user["username"]
                self.password = db_user["password"]
                self.email = db_user["email"]
                self.organizations = db_user["organizations"]
                self.groups = db_user["groups"]

                if return_user:
                    return {
                        "username": self.username,
                        "password": self.password,
                        "email": self.email,
                        "organizations": self.organizations,
                        "groups": self.groups
                    }

                else:
                    return self

    @rethinkdb_connection
    def create(self, username, password, email, conn):
        """
        Create a new user in the DB
        """
        if not isinstance(username, str):
            raise TypeError("Username needs to be a string!")

        elif not isinstance(password, str):
            raise TypeError("Password needs to be a string!")

        elif not isinstance(email, str):
            raise TypeError("Email needs to be a string!")

        else:
            try:
                self.get(username)

            except KeyError:
                result = r.table("users").insert({
                    "username": username,
                    "password": encrypt_password(password),
                    "email": email,
                    "organizations": [],
                    "groups": []
                }).run(conn)

                if result["inserted"] == 1:
                    return True

                else:
                    return False

            else:
                raise ValueError("There's already an user with this username!")

    @rethinkdb_connection
    def update(self, conn, new_password=None, new_email=None):
        """
        Update a specific user from the DB
        """
        if not isinstance(new_password, str) and not isinstance(new_password, type(None)):
            raise TypeError("Password needs to be a string!")

        elif not isinstance(new_email, str) and not isinstance(new_email, type(None)):
            raise TypeError("Email needs to be a string!")

        elif not new_password and not new_email:
            raise ValueError("You need make some changes!")

        else:
            to_update = {}
            if new_password:
                to_update["password"] = encrypt_password(new_password)

            if new_email:
                to_update["email"] = new_email

            result = r.table("users").get(self.username).update(to_update).run(conn)

            if result["replaced"] == 1:
                return True

            else:
                return False

    @rethinkdb_connection
    def add_organization(self, organization_id, conn):
        """
        Add an user to an organization
        """
        if not isinstance(organization_id, str):
            raise TypeError("Organization ID needs to be a string!")

        else:
            # TODO: Replace with the Organization model
            db_organization = r.table("organizations").get(organization_id).run(conn)
            if not db_organization:
                raise KeyError("The organization wasn't found in the DB!")

            else:
                try:
                    self.organizations.index(organization_id)

                except ValueError:
                    result = r.table("users").get(self.username).update({
                        "organizations": r.row["organizations"].append(organization_id)
                    }).run(conn)

                    if result["replaced"] == 1:
                        return True

                    else:
                        return False

                else:
                    raise ValueError("The user is already in the organization!")

    @rethinkdb_connection
    def remove_organization(self, organization_id, conn):
        """
        Remove an user from an organization
        """
        if not isinstance(organization_id, str):
            raise TypeError("Organization ID needs to be a string!")

        else:
            # TODO: Replace with the Organization model
            db_organization = r.table("organizations").get(organization_id).run(conn)
            if not db_organization:
                raise KeyError("The organization wasn't found in the DB!")

            else:
                try:
                    organization_index = self.organizations.index(organization_id)

                except ValueError:
                    raise ValueError("The user isn't in the organization!")

                else:
                    result = r.table("users").get(self.username).update({
                        "organizations": r.row["organizations"].delete_at(organization_index)
                    }).run(conn)

                    if result["replaced"] == 1:
                        return True

                    else:
                        return False

    @rethinkdb_connection
    def add_group(self, group_id, conn):
        """
        Add an user to a group
        """
        if not isinstance(group_id, str):
            raise TypeError("Group ID needs to be a string!")

        else:
            # TODO: Replace with the Group model
            db_group = r.table("groups").get(group_id).run(conn)
            if not db_group:
                raise KeyError("The group wasn't found in the DB!")

            else:
                try:
                    self.groups.index(group_id)

                except ValueError:
                    result = r.table("users").get(self.username).update({
                        "groups": r.row["groups"].append(group_id)
                    }).run(conn)

                    if result["replaced"] == 1:
                        return True

                    else:
                        return False

                else:
                    raise ValueError("The user is already in the group!")

    @rethinkdb_connection
    def remove_group(self, group_id, conn):
        """
        Remove an user from a group
        """
        if not isinstance(group_id, str):
            raise TypeError("Group ID needs to be a string!")

        else:
            # TODO: Replace with the Group model
            db_group = r.table("groups").get(group_id).run(conn)
            if not db_group:
                raise KeyError("The group wasn't found in the DB!")

            else:
                try:
                    group_index = self.groups.index(group_id)

                except ValueError:
                    raise ValueError("The user isn't in the group!")

                else:
                    result = r.table("users").get(self.username).update({
                        "groups": r.row["groups"].delete_at(group_index)
                    }).run(conn)

                    if result["replaced"] == 1:
                        return True

                    else:
                        return False
