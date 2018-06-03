#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection

class Organization:
    """
    Organization model. This class should have all the operations related with the organizations
    """

    @rethinkdb_connection
    def get(self, organization_id, conn, return_organization=False):
        """
        Retrieve a specific organization from the DB
        """
        if not isinstance(organization_id, str):
            raise TypeError("Organization ID needs to be a string!")

        else:
            db_organization = r.table("organizations").get(organization_id).run(conn)
            if not db_organization:
                raise KeyError("The organization wasn't found in the DB!")

            else:
                self.organization_id = organization_id
                self.name = db_organization["name"]
                self.description = db_organization["description"]
                self.groups = db_organization["groups"]

                if return_organization:
                    return {
                        "name": self.name,
                        "description": self.description,
                        "groups": self.groups
                    }

                else:
                    return self

    @rethinkdb_connection
    def create(self, name, description, conn):
        """
        Create a new organization in the DB
        """
        if not isinstance(name, str):
            raise TypeError("Name needs to be a string!")

        elif not isinstance(description, str):
            raise TypeError("Description needs to be a string!")

        else:
            result = r.table("organizations").insert({
                "name": name,
                "description": description,
                "groups": []
            }).run(conn)

            return result["inserted"] == 1

    @rethinkdb_connection
    def update(self, conn, new_name=None, new_description=None):
        """
        Update a specific organization from the DB
        """
        if not isinstance(new_name, str):
            raise TypeError("Name needs to be a string!")

        elif not isinstance(new_description, str):
            raise TypeError("Description needs to be a string!")

        elif not new_name and not new_description:
            raise ValueError("You need to make some changes!")

        elif new_name == self.name:
            raise ValueError("You need to provide a different name in order to update it!")

        elif new_description == self.description:
            raise ValueError("You need to provide a different description in order to update it!")

        else:
            to_update = {}
            if new_name:
                to_update["name"] = new_name

            if new_description:
                to_update["description"] = new_description

            result = r.table("organizations").get(self.organization_id).update(to_update).run(conn)

            return result["replaced"] == 1

    @rethinkdb_connection
    def delete(self, conn):
        """
        Delete a specific organizaiton from the DB
        """
        result = r.table("organizations").get(self.organization_id).delete().run(conn)

        return result["deleted"] == 1

    @rethinkdb_connection
    def add_group(self, group_id, conn):
        """
        Add a group to an organization
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
                    result = r.table("organizations").get(self.organization_id).update({
                        "groups": r.row["groups"].append(group_id)
                    }).run(conn)

                    return result["replaced"] == 1

                else:
                    raise ValueError("The group is already in the organization!")

    @rethinkdb_connection
    def remove_group(self, group_id, conn):
        """
        Remove a group from an organization
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
                    raise ValueError("The group isn't in the organization!")

                else:
                    result = r.table("organizations").get(self.organization_id).update({
                        "groups": r.row["groups"].delete_at(group_index)
                    }).run(conn)

                    return result["replaced"] == 1
