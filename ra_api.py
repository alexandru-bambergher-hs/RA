# filename: ra_api.py
"""A basic (single function) API written using hug"""
import hug
from locktest import *

JSON_DATA = []
RESOURCE_JSON_FILE = 'input_resources.json'

sample_output1 =  [
   {
      "status":"free",
      "res":{
         "staging":[
            "user1:password123"
         ]
      }
   }
]

sample_output2 =  [
   {
      "status":"busy",
      "res":{
         "production":[
            "user3:password321"
         ]
      }
   }
]

sample_output3 =  [
   {
      "status":"NA",
      "res":{
         "staging":[
            "user2:password321",
            "user1:password321"
         ]
      }
   }
]

@hug.startup()
def get_json_data(api):
    """Load initial JSON data to the api on startup"""
    global JSON_DATA
    with open(RESOURCE_JSON_FILE, encoding='utf-8') as data_file:
        JSON_DATA = json.loads(data_file.read())

@hug.get()
def lock(res, num:hug.types.number=1):
    """Lock a number of resources of certain type!"""
    if num == 3:
        return sample_output3
    elif num == 2:
        return sample_output2
    elif num == 1:
        return sample_output1
    else:
        return JSON_DATA

@hug.post()
def unlock(body):
    """Unlock resource(s) in json format!"""
    return body

def is_json_valid(inputjson):
    try:
        json_object = json.loads(inputjson)
    except ValueError:
        return False
    return True

def json_to_dict(inputjson):
    return json.loads(inputjson)

def dict_to_json(inputdict):
    return json.dumps(inputdict)
