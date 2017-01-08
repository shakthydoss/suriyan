import json

import requests
import rest.dao.mongodb as connection_manager_mongo
from flask import current_app


def authenticate(data):
    current_app.logger.debug("Entering method authenticate of auth_dao.")
    headers = {'content-type': 'application/json'}
    r = requests.post('http://localhost/auth/authenticateUser/', data=json.dumps(data), headers=headers)
    if json.loads(r.content)["status"] == 200:
        print json.loads(r.content)["data"]["uid"]
        db, connection = connection_manager_mongo.get_connection()
        uid = json.loads(r.content)["data"]["uid"]
        fltr = {"uid": uid}
        result = db.usr.find_one(fltr)
        del result["_id"]
        result["access_token"] = json.loads(r.content)["data"]["access_token"]
        tmp = dict()
        tmp["status"] = "200"
        tmp["data"] = result
        tmp = json.dumps(tmp)
        return tmp
    return r.content


def logout(data):
    current_app.logger.debug("Entering method logout of auth_dao.")
    headers = {'content-type': 'application/json'}
    r = requests.post('http://localhost/auth/logout/', data=json.dumps(data), headers=headers)
    return r.content


def authenticate_token(data):
    current_app.logger.debug("Entering method logout of auth_dao.")
    headers = {'content-type': 'application/json'}
    r = requests.post('http://localhost/auth/authenticateToken/', data=json.dumps(data), headers=headers)
    return r.content
