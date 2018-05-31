#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from flask_restful import Resource, reqparse
import rethinkdb as r

# Decorators imports
from api.decorators.rethinkdb_decorators import rethinkdb_connection


# Menu Entry resource
class MenuEntry(Resource):

    # GET
    @rethinkdb_connection
    def get(self, menu_id, entry_position, conn):
        """
        Get an specific entry using it's position on the menu
        """
        menu = r.table("menus").get(menu_id).run(conn)

        if menu:
            for entry in menu["entries"]:
                if entry["position"] == entry_position:
                    return {"response": entry}, 200

            return {"response": "Error 404! The entry wasn't found inside the menu!"}, 404

        else:
            return {"response": "Error 404! The menu wasn't found!"}, 404

    # POST
    @rethinkdb_connection
    def post(self, menu_id, entry_position, conn):
        """
        Create a new entry in a specific position in an existing menu. If there's already an entry in that position,
        move that one and all the following one position down and insert the new one there.
        """
        parser = reqparse.RequestParser()
        parser.add_argument("type", required=True, type=str, help="This is the type of entry. It can be 'image' or 'separator'")
        parser.add_argument("image_id", type=str, help="This is the id of the image of the entry. Just avaliable if the type is 'image'")
        parser.add_argument("content", type=str, help="This is the content (the text that shows) the separator. Just avaliable if the type is 'separator'")
        args = parser.parse_args()

        entries = r.table("menus").get(menu_id).run(conn)["entries"]

        if entries or entries == []:
            if args["type"] == "separator" and not args["content"]:
                return {"response": "Error 400! If you want to add a separator, it needs to have content! (The text that this will show)"}, 400

            elif args["type"] == "separator" and args["image_id"]:
                return {"response", "Error 400! You can't provide an image id for a separator!"}, 400

            elif args["type"] == "image" and not args["image_id"]:
                return {"response": "Error 400! If you want to add an image, it needs to have an image id!"}, 400

            elif args["type"] == "image" and args["content"]:
                return {"response": "Error 400! You can't provide content for an image!"}, 400

            else:
                new_entry = {
                    "type": args["type"]
                }
                if args["content"]: new_entry["content"] = args["content"]
                if args["image_id"]: new_entry["image_id"] = args["image_id"]

                entries.insert(entry_position, new_entry)

                result = r.table("menus").get(menu_id).update({"entries": entries}).run(conn)

                if result["replaced"] == 1:
                    return {"response": "Successfully added the entry to the menu!"}, 200

                else:
                    return {"response": "Error 500! Internal server error!"}, 500

        else:
            return {"response": "Error 404! The menu wasn't found!"}, 404

    # PUT
    @rethinkdb_connection
    def put(self, menu_id, entry_position, conn):
        """
        Update the content field or change the position of an existing menu entry in an existing menu
        """
        parser = reqparse.RequestParser()
        parser.add_argument("content", type=str, help="This is the content (the text that shows) the separator. Just avaliable if the type is 'separator'")
        parser.add_argument("new_position", type=int, help="This is the new position where the entry is going to be on")
        args = parser.parse_args()

        entries = r.table("menus").get(menu_id).run(conn)["entries"]

        if entries or entries == []:
            try:
                # Check if there's already an entry in that position
                entry_to_update = entries[entry_position]

            # There's no entry in that position
            except IndexError:
                return {"response": "Error 404! The entry wasn't found in the menu!"}, 404

            # There's an entry in that position
            else:
                if args["content"] and entry_to_update["type"] != "separator":
                    return {"response": "Error 400! You can't provide content for an image!"}, 400

                else:
                    if args["content"]:
                        entry_to_update["content"] = args["content"]

                    entries.insert(args["new_position"], entries.pop(entry_position))
                    result = r.table("menus").get(menu_id).update({"entries": entries}).run(conn)

                    if result["replaced"] == 1:
                        return {"response": "Successfully updated the entry!"}, 200

                    else:
                        return {"response": "Error 500! Internal server error!"}, 500

        else:
            return {"response": "Error 404! The menu wasn't found!"}, 404

    # DELETE
    @rethinkdb_connection
    def delete(self, menu_id, entry_position, conn):
        """
        Delete an existing menu entry in an existing menu
        """
        entries = r.table("menus").get(menu_id).run(conn)["entries"]

        if entries or entries == []:
            try:
                # Check if there's already an entry in that position (and delete it)
                del entries[entry_position]

            # There's no entry in that position
            except IndexError:
                return {"response": "Error 404! The entry wasn't found in the menu!"}, 404

            # There was an entry on that position
            else:

                result = r.table("menus").get(menu_id).update({"entries": entries}).run(
                    conn)

                if result["replaced"] == 1:
                    return {"response": "Successfully removed the entry from the menu!"}, 200

                else:
                    return {"response": "Error 500! Internal server error!"}, 500

        else:
            return {"response": "Error 404! The menu wasn't found!"}, 404