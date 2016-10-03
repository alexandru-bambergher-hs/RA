# filename: ra_api.py
"""A basic (single function) API written using hug"""
import hug

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

@hug.get()
def lock(res, num:hug.types.number=1):
    """Lock a number of resources of certain type!"""
    if num == 3:
        return sample_output3
    elif num == 2:
        return sample_output2
    else:
        return sample_output1

@hug.post()
def unlock(body):
    """Unlock resource(s) in json format!"""
    return body
