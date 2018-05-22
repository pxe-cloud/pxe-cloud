#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Resources imports
from api.resources.users_resource import Users
from api.resources.user_resource import User
from api.resources.users.user_organization_resource import UserOrganization
from api.resources.users.user_group_resource import UserGroup
from api.resources.organizations_resource import Organizations
from api.resources.organization_resource import Organization
from api.resources.organizations.organization_group_resource import OrganizationGroup
from api.resources.groups_resource import Groups
from api.resources.group_resource import Group
from api.resources.menus_resource import Menus
from api.resources.menu_resource import Menu
from api.resources.menus.menu_entry_resource import MenuEntry
from api.resources.images_resource import Images
from api.resources.image_resource import Image
from api.resources.boot.auth_resource import BootAuth
from api.resources.boot.organizations_script_resource import OrganizationsScript
from api.resources.boot.groups_script_resource import GroupsScript
from api.resources.boot.menu_script_resource import MenuScript
from api.resources.boot.return_image_resource import ReturnImage


# Add all the endpoints to the API
def add_endpoints(api):
    api.add_resource(Users, "/users")
    api.add_resource(User, "/user/<username>")
    api.add_resource(UserOrganization, "/user/<username>/organization/<organization_id>")
    api.add_resource(UserGroup, "/user/<username>/group/<group_id>")
    api.add_resource(Organizations, "/organizations")
    api.add_resource(Organization, "/organization/<organization_id>")
    api.add_resource(OrganizationGroup, "/organization/<organization_id>/group/<group_id>")
    api.add_resource(Groups, "/groups")
    api.add_resource(Group, "/group/<group_id>")
    api.add_resource(Menus, "/menus")
    api.add_resource(Menu, "/menu/<menu_id>")
    api.add_resource(MenuEntry, "/menu/<menu_id>/entry/<int:entry_position>")
    api.add_resource(Images, "/images")
    api.add_resource(Image, "/image/<image_id>")
    api.add_resource(BootAuth, "/boot")
    api.add_resource(OrganizationsScript, "/boot/<username>")
    api.add_resource(GroupsScript, "/boot/<username>/<organization_id>")
    api.add_resource(MenuScript, "/boot/<username>/<organization_id>/<group_id>")
    api.add_resource(ReturnImage, "/boot/<username>/<organization_id>/<group_id>/<image_id>")
