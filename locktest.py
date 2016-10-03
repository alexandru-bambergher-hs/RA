import threading
import json

lock = threading.RLock()
filename = "input_resources.json"


def lock_credentials(medium = "staging"):
    # TODO:
    lock.acquire()
    try:
    # ... fetch data for first part from shared object
        text = open(filename)
        parsed_json = json.load(text)

        for credential in parsed_json[medium]:
            credentials = credential.split(":")
            # print credentials

    finally:
        lock.release()
    # return data


lock_credentials()