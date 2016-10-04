from collections import defaultdict

def lock_credentials(JSON_DATA, res_type = None, res_value = None):
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

def unlock_credentials(JSON_DATA, res_type = None, res_value = None):
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

# #testing the JSON import
# import json
# res_value_JSON_FILE = 'input_resources.json'

# def load_json_data():
#     """Load initial JSON data to the api on startup"""
#     global JSON_DATA
#     with open(res_value_JSON_FILE, encoding='utf-8') as data_file:
#         JSON_DATA = json.loads(data_file.read())

# load_json_data()

# lock_credentials(JSON_DATA, res_type="staging", res_value="empty")
# print(lock_credentials(JSON_DATA, res_type="staging", res_value="user1"))
# lock_credentials(JSON_DATA, res_type="staging", res_value="user2")
# lock_credentials(JSON_DATA, res_type="production", res_value="user3")
# lock_credentials(JSON_DATA, res_type="production", res_value="user3")
# lock_credentials(JSON_DATA, res_type="production", res_value="user4")
# lock_credentials(JSON_DATA, res_type="production")
# lock_credentials(JSON_DATA)

# print(JSON_DATA)

# unlock_credentials(JSON_DATA, res_type="staging", res_value="empty")
# unlock_credentials(JSON_DATA, res_type="staging", res_value="user1")
# unlock_credentials(JSON_DATA, res_type="production", res_value="user2")
# unlock_credentials(JSON_DATA, res_type="production", res_value="user3")
# unlock_credentials(JSON_DATA, res_type="production", res_value="user3")
# unlock_credentials(JSON_DATA, res_type="production", res_value="user4")
# unlock_credentials(JSON_DATA, res_type="staging")
# unlock_credentials(JSON_DATA)

# print(JSON_DATA)
