#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Methods imports
from api.methods.files_methods import read_settings

# Resources imports
from api.resources.auth_resource import Auth
from api.resources.users_resource import Users
from api.resources.user_resource import User
from api.resources.organizations_resource import Organizations
from api.resources.organization_resource import Organization
from api.resources.groups_resource import Groups
from api.resources.group_resource import Group
from api.resources.boot.organizations_script_resource import OrganizationsScript
from api.resources.boot.groups_script_resource import GroupsScript
from api.resources.boot.menu_script_resource import MenuScript
from api.resources.boot.return_image_resource import ReturnImage


# Add all the endpoints to the API
def add_endpoints(api):
    root = read_settings("api")["base_url"]
    api.add_resource(Auth, f"{root}auth")
    api.add_resource(Users, f"{root}users")
    api.add_resource(User, f"{root}user/<username>")
    api.add_resource(Organizations, f"{root}organizations")
    api.add_resource(Organization, f"{root}organization/<organization_id>")
    api.add_resource(Groups, f"{root}groups")
    api.add_resource(Group, f"{root}group/<group_id>")
    api.add_resource(OrganizationsScript, f"{root}boot/<username>")
    api.add_resource(GroupsScript, f"{root}boot/<username>/<organization_id>")
    api.add_resource(MenuScript, f"{root}boot/<username>/<organization_id>/<group_id>")
    api.add_resource(ReturnImage, f"{root}boot/<username>/<organization_id>/<group_id>/<image_id>")
