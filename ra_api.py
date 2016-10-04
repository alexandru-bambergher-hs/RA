# filename: ra_api.py
"""A basic (single function) API written using hug"""
import hug
from locktest import *

JSON_DATA = []
RESOURCE_JSON_FILE = 'input_resources.json'

@hug.startup()
def get_json_data(api):
    """Load initial JSON data to the api on startup"""
    global JSON_DATA
    JSON_DATA = load_json_file(RESOURCE_JSON_FILE, JSON_DATA)
    freeup_resources(JSON_DATA)

@hug.get()
def info(res_type:hug.types.text=None, res_value:hug.types.text=None):
    """Lookup a resources of certain type and value!"""
    return lookup_resource(JSON_DATA, res_type, res_value)

@hug.get()
def lock(res_type, res_value:hug.types.text=None):
    """Lock a number of resources of certain type and value!"""
    return lock_resource(JSON_DATA, res_type, res_value)

@hug.post()
def unlock(body):
    """Unlock resource(s) in json format!"""
    res_type = next(iter(body))
    res_value = next(iter(body[res_type]))
    return unlock_resource(JSON_DATA, res_type, res_value)
