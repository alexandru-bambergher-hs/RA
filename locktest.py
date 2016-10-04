from collections import defaultdict
import json

# lock = threading.RLock()
# filename = "input_resources.json"
#
# RESOURCE_JSON_FILE = 'input_resources.json'
#
# def get_json_data():
#     """Load initial JSON data to the api on startup"""
#     global JSON_DATA
#     with open(RESOURCE_JSON_FILE, encoding='utf-8') as data_file:
#         JSON_DATA = json.loads(data_file.read())

def lock_credentials(JSON_DATA, user=None, medium = "staging"):

    if JSON_DATA[medium][user].get("status") != "busy":
        # lock.acquire()
        try:
            JSON_DATA[medium][user]["status"] = "busy"
            print("resource %s locked" % user)
            print(JSON_DATA[medium])

        except Exception as e:
            raise e

        return True
    else:
        print("Couldn't acquire lock")
        return False

def unlock_credentials(JSON_DATA, user=None, medium = "staging"):
    if JSON_DATA[medium][user].get("status") == "busy":
        try:
            JSON_DATA[medium][user]["status"] = "free"
            # lock.release()
        except Exception as e:
            raise e
        print("Resource %s unlocked", user)
        return True
    else:
        print("Resource %s already free", user)
        return False

# testing the JSON import
# lock_credentials(JSON_DATA,user="user2")
# lock_credentials(JSON_DATA,user="user2")
# unlock_credentials(JSON_DATA, user="user2")
# lock_credentials(JSON_DATA,user="user2")
