emp = dict()         # Encoding:python -> JSon
emp['id'] = 1
emp['name'] = 'Mary'
import datetime
emp['birthday'] = datetime.date(2000,1,1)
print(emp,type(emp))
import json
json_repr = json.dumps(emp,default=str)
print(json_repr,type(json_repr))

