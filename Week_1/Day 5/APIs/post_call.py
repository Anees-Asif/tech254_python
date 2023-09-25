# Post request to postcode api

import requests
import json

json_body = json.dumps({"postcodes": ["PRE3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers= headers, data=json_body)

print(post_multi_req.json())

