import json

import rest.dao.mongodb as connection_manager_mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import current_app


def get_tags():
    current_app.logger.debug("Entering method get_tags of tag_dao")
    db, connection = connection_manager_mongo.get_connection()
    result = json.loads(dumps(db.tag.find({"$query": {}, "$orderby": {"is_active": -1, "name": 1}})))
    current_app.logger.debug("Exiting method get_tags of tag_dao")
    return result


def get_tag_by_id(tag_id):
    current_app.logger.debug("Entering method get_tag_by_id of tag_dao")
    db, connection = connection_manager_mongo.get_connection()
    result = db.tag.find_one({"_id": ObjectId(tag_id)})
    result = json.loads(dumps(result))
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method get_tag_by_id of tag_dao")
    return result


def save_tag(data):
    current_app.logger.debug("Entering method save_tag of tag_dao")
    db, connection = connection_manager_mongo.get_connection()
    val = {
        "name": data["name"],
        "description": data["description"],
        "is_active": data["is_active"]
    }
    db.tag.insert(val)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method save_tag of tag_dao")
    return 0;


def update_tag(data):
    current_app.logger.debug("Entering method update_tag of tag_dao")
    db, connection = connection_manager_mongo.get_connection()
    fltr = {"_id": ObjectId(data["tag_id"])}
    val = {
        "name": data["name"],
        "description": data["description"],
        "is_active": data["is_active"]
    }
    db.tag.update(fltr, val)
    connection_manager_mongo.close_connection(connection)
    current_app.logger.debug("Exiting method update_tag of tag_dao")
    return 0;


def delete_tag():
    return 0;
