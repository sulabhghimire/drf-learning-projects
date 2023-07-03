import requests
import json

URL = 'http://127.0.0.1:8000/addstu/'

data = {'name' : 'Sulabh', 'roll' : '47', 'city':'Pokhara'}
json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

r_data = r.json()

print(r_data)