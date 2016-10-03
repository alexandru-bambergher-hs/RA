# filename: ra_api.py
"""A basic (single function) API written using hug"""
import hug

sample_output =  [
   {
      "status":"free",
      "res":{
         "staging":[
            "user1:password123"
         ]
      }
   }
]

@hug.get()
def get(res, num:hug.types.number=1):
    """Get a number of resources of certain type!"""
    return sample_output
