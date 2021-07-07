json_str= '{"object": "page", "entry": [{"id": "2023215964389640", "time": 1533549645855,"messaging": [{"sender": {"id": "1714516545284315"}, "recipient": {"id":"2023215964389640"},"timestamp": 1533549645608, "message": {"mid": "MeaU_wmMqoAamx1U2oGex60t0p58rg9q8ZeHlr9SZ4u1HU_Xvk0D2dxaPiHI3V-ryqe225kYA5lvX3XSDqYb0A","seq": 8332, "text": "aaa"}}]}]}'
import json
dict = json.loads(json_str)
entry = dict['entry']
for a in entry:
    messaging = a['messaging']
    for b in messaging:
        number = b['sender']
        print(number['id'])



#找出1714516545284315 作業