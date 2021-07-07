import requests
# r = requests.get('http://127.0.0.1:5000')
#DoS: Denial of Service(做壓力測試)
while True:
    r = requests.post('http://127.0.0.1:5000/add',data={'a':10,'b':20})
    print(r.text,type(r.text))
