# Encoding: python dict-> json,

emp = dict()
emp['id'] = 1
emp['name'] = 'Mary'
import datetime
emp['birthdate'] = datetime.date(2000,1,1)
print(emp,type(emp))

import json
json_rep = json.dumps(emp,default = str)
print(json_rep,type(json_rep))