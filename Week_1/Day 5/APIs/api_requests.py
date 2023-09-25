# api requests

import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req)
print(post_codes_req.headers)
print(post_codes_req.content)

# Long way
# post_codes_dict = json.loads(post_codes_req.content)
# print(post_codes_dict)

# Short way
print(post_codes_req.json()) # Use inbuilt method