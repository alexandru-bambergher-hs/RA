# filename: ra_api.py
"""A basic (single function) API written using hug"""
import hug

@hug.get('/get')
def get(res, num:hug.types.number=1):
    """Get a number of resources of certain type!"""
    return "Get {num} resource(s) of type {res}!".format(**locals())