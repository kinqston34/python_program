#encoding
emp = dict()
emp['id'] = 1
emp['name'] = 'Mary'
emp['addr'] = ['Kao','TNN']
import json
json_rep = json.dumps(emp)
print(json_rep,type(json_rep))