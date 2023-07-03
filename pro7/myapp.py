import requests, json

URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data= {}
    if id is not None:
        data = {'id' : id}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=headers, data = json_data)
    out_data = r.json()
    print(out_data)

# get_data()

def post_data():
    data = {
        'name' : 'Sohit', 
        'roll': 99, 
        'city' : 'Rachi' 
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data = json_data)
    out_data = r.json()
    print(out_data)

# post_data()

def update_data():
    data = {'id' : 1, 'name' : 'Samir Lamsal', 'roll':40, 'city' : 'Palpa' }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data = json_data)
    out_data = r.json()
    print(out_data)

# update_data()

def delete_data():
    data = {'id' : 6}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers,data = json_data)
    out_data = r.json()
    print(out_data)

delete_data()