#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import pytest


class TestOrganizationModelCreate:
    """
    Test all the possible responses and errors of the create() method of the Organization model
    """
    def test_clear_table(self, import_module):
        """
        Clear the table before running all the tests
        """
        clear_table = import_module(path="api.methods.rethinkdb_methods", module="clear_table")
        clear_table("organizations")

    def test_create_name_non_string(self, import_module, organization):
        """
        Try creating an organization without passing a string in the name
        """
        Organization = import_module(path="api.models.organization", module="Organization")

        with pytest.raises(TypeError) as excinfo:
            Organization().create(1234, organization["description"])

        assert "Name needs to be a string!" in str(excinfo.value)

    def test_create_description_non_string(self, import_module, organization):
        """
        Try creating an organization without passing a string or nothing in the description
        """
        Organization = import_module(path="api.models.organization", module="Organization")

        with pytest.raises(TypeError) as excinfo:
            Organization().create(organization["name"], 1234)

        assert "Description needs to be a string or be empty!" in str(excinfo.value)

    def test_create(self, import_module, organization):
        """
        Create a new organization
        """
        Organization = import_module(path="api.models.organization", module="Organization")

        assert Organization().create(organization["name"], organization["description"])
