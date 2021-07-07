#deconding: JSON -> Python
json_str = '{"id":1,"name":"Mary","birthday":"2000-01-01"}'
import json
def date_parser(d):
    for k,v in d.items():
        if k == 'birthday' and isinstance(v,str):
            import datetime
            #parse 解析
            birthday = datetime.datetime.strptime(d['birthday'],'%Y-%m-%d')
            d['birthday'] = birthday
    return d
dic = json.loads(json_str,object_hook=date_parser)
# print(dic,type(dic))
# print(dic['name'])
print(dic['birthday'],type(dic['birthday']))