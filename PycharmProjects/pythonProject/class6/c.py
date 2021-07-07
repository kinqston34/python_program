#decoding JSON-> python dict
def date_parser(d):
    import datetime
    #birthdate = datetime.datetime.strptime(d['birthdate'],'%Y-%m-%d')
    #d['birthdate'] = birthdate
    d['birthdate'] = datetime.datetime.fromisoformat(d['birthdate'])
    return d

json_str = '{"birthdate": "2000-01-01T13:00:00"}'
import  json
dic = json.loads(json_str,object_hook=date_parser)
#print(dic['id'],dic['name'])
print(dic['birthdate'],type(dic['birthdate']))
