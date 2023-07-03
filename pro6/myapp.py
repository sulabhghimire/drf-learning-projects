import requests, json

URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data= {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data = json_data)
    out_data = r.json()
    print(out_data)

# get_data()

def post_data():
    data = {'name' : 'Sohit', 'roll': 99, 'city' : 'Rachi' }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data = json_data)
    out_data = r.json()
    print(out_data)

post_data()

def update_data():
    data = {'id' : 1, 'name' : ' Kumar Chalise', 'roll':230, 'city' : 'Pokhara' }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data = json_data)
    out_data = r.json()
    print(out_data)

# update_data()

def delete_data():
    data = {'id' : 1}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data = json_data)
    out_data = r.json()
    print(out_data)

# delete_data()