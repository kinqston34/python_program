json_str = '{"id": 1, "name": "Mary", "addr": [{"county": "Kao", "distinc": "Lingya"}, {"county": "TNN", "distinc": "Dong"}]}'
import json
dic = json.loads(json_str)
print(dic['name'])
addr = dic['addr']
print(type(addr))
for d in addr:
    print(d['county'])