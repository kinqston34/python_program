import requests
r = requests.get('https://www.googleapis.com/books/v1/volumes?q=python')
json = r.json()
for item in json['items']:
    print(item['volumeInfo']['title'])
    print(item['volumeInfo'].get('subtitle',''))