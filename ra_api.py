# filename: ra_api.py
"""A basic (single function) API written using hug"""
import hug
import json
from locktest import *

JSON_DATA = []
RESOURCE_JSON_FILE = 'input_resources.json'

@hug.startup()
def get_json_data(api):
    """Load initial JSON data to the api on startup"""
    global JSON_DATA
    with open(RESOURCE_JSON_FILE, encoding='utf-8') as data_file:
        JSON_DATA = json.loads(data_file.read())

@hug.get()
def lock(res_type, res_value, num:hug.types.number=1):
    """Lock a number of resources of certain type!"""
    return lock_credentials(JSON_DATA, res_type, res_value)

@hug.post()
def unlock(body):
    """Unlock resource(s) in json format!"""
    res_type = next(iter(body))
    res_value = next(iter(body[res_type]))
    return unlock_credentials(JSON_DATA, res_type, res_value)
