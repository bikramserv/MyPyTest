from contextlib import nullcontext

import requests
import pytest

#Base url of the API

API_URL = "https://app-as-webhook-test.azurewebsites.net/"



def test_get_resp():

 res = requests.get(API_URL)
 assert res.status_code == 200

 json_data = res.json()

 # print (json_data)
 if json_data and json_data.get("event") == "verification.complete":
     print("verification complete event is found")

     for verification_id in json_data ["data"]["id"]:
         print (f"The id of completed verifications are : {verification_id}")
 elif json_data.get ("event") == "verification.failed":
     print ("verification failed")

     #print(json_data)
 else:
     print("No tests executed")

 # Validate the key and value check partial

