import requests

URL = 'http://127.0.0.1:8000/stuinfo/'

r = requests.get(URL)

data = r.json()

print(data)