json_str = '{"id": 1, "name": "Mary", "addr": ["Kao", "TNN"]}'
import json
dic = json.loads(json_str)
print(dic['name'])
addr = dic['addr']
print(type(addr))
for a in addr:
    print(a)