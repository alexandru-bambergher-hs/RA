import json
from collections import defaultdict

def load_json_file(RESOURCE_JSON_FILE, JSON_DATA):
    with open(RESOURCE_JSON_FILE, encoding='utf-8') as data_file:
        JSON_DATA = json.loads(data_file.read())
    return JSON_DATA

def freeup_resources(JSON_DATA):
    for res_type in JSON_DATA.keys():
        obj_type = JSON_DATA[res_type]
        for res_value in obj_type.keys():
            JSON_DATA[res_type][res_value]["status"] = "free"

def find_res_name(JSON_DATA, res_match):
    for res_type, res_value in JSON_DATA.items():
        if res_type == res_match:
            obj_type = JSON_DATA[res_type]
            for res_value in obj_type.keys():
                if JSON_DATA[res_type][res_value].get("status") == "free":
                    return res_value

def lookup_resource(JSON_DATA, res_type = None, res_value = None):
    if not res_type:
        return JSON_DATA

    if not res_value:
        return {res_type:JSON_DATA[res_type]}

    if not JSON_DATA.get(res_type):
        print("Resource type %s not defined" % res_type)
        return {res_type:{res_value:{"status": "NA"}}}

    if JSON_DATA[res_type].get(res_value):
        print("Lookup resource %s and value %s" % (res_type,res_value))
        return {res_type:{res_value:JSON_DATA[res_type][res_value]}}
    else:
        print("Resource %s not found" % res_value)
        return {res_type:{res_value:{"status": "NA"}}}

def lock_resource(JSON_DATA, res_type = None, res_value = None):
    if not res_value and res_type:
        res_value = find_res_name(JSON_DATA, res_type)

    if not JSON_DATA.get(res_type):
        print("Resource type %s not defined" % res_type)
        return {res_type:{res_value:{"status": "NA"}}}

    if JSON_DATA[res_type].get(res_value):
        if JSON_DATA[res_type][res_value].get("status") != "busy":
            try:
                JSON_DATA[res_type][res_value]["status"] = "busy"
                print("Resource %s locked" % res_value)
            except Exception as e:
                print("Resource %s not found" % res_value)
                return {res_type:{res_value:{"status": "NA"}}}
            return {res_type:{res_value:JSON_DATA[res_type][res_value]}}
        else:
            print("Already locked for %s" % res_value)
            return {res_type:{res_value:JSON_DATA[res_type][res_value]}}
    else:
        print("Resource %s not found" % res_value)
        return {res_type:{res_value:{"status": "NA"}}}

def unlock_resource(JSON_DATA, res_type = None, res_value = None):
    if not JSON_DATA.get(res_type):
        print("Resource type %s not defined" % res_type)
        return {res_type:{res_value:{"status": "NA"}}}

    if JSON_DATA[res_type].get(res_value):
        if JSON_DATA[res_type][res_value].get("status") != "free":
            try:
                JSON_DATA[res_type][res_value]["status"] = "free"
                print("Resource %s unlocked" % res_value)
            except Exception as e:
                print("Resource %s not found" % res_value)
                return {res_type:{res_value:{"status": "NA"}}}
            return {res_type:{res_value:JSON_DATA[res_type][res_value]}}
        else:
            print("Resource %s already unlocked" % res_value)
            return {res_type:{res_value:JSON_DATA[res_type][res_value]}}
    else:
        print("Resource %s not found" % res_value)
        return {res_type:{res_value:{"status": "NA"}}}
