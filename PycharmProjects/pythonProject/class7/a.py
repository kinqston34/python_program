#encoding
emp = dict()
emp['id'] = 1
emp['name'] = 'Mary'
emp['addr'] = ['Kao','TNN']
addr1 = {'county':'Kao','distinc':'Lingya'}
addr2 = {'county':'TNN','distinc':'Dong'}
emp['addr'] = [addr1,addr2]
import json
json_rep = json.dumps(emp)
print(json_rep,type(json_rep))
