# ISOFormat: 3.7 之後
import datetime
emp = dict()
emp['birthdate'] = datetime.datetime(2000,1,1,13,0,0)
import json
def convert_to_json(obj):
    if isinstance(obj,(datetime.date,datetime.datetime)):
        return  obj.isoformat()
print(json.dumps(emp,default=convert_to_json))