import requests
r = requests.get('http://127.0.0.1:8080/')
print(r.text,type(r.text))
json = r.json()
print(json,type(json))
print(json['id'],json['name'])