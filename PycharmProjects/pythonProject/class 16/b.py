import requests
r = requests.get('http://127.0.0.1:5000/')
# import json
# json = json.loads(r.text)
json = r.json()
print(json['id'])
print(json['name'])