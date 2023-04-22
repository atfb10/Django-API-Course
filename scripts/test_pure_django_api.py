'''
Author: Adam forestier
Date: April 22, 2023
description: test pure django api using requests library

Python by default treats data as a string
.json() from 
'''

import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates"

def get_list(b=BASE_URL, e=ENDPOINT):
    path = b+e
    data = requests.get(path).json() # Gets list of dictionaries
    for d in data:
        print(d['content'])
    return data

def get_detail_by_content(content: str, b=BASE_URL, e=ENDPOINT):
    path = b+e
    data = requests.get(path).json()
    for d in data:
        if d['content'] == content:
            return d
    return 'Update Not Found'

# This fails, because of Django's built in protection -> Doesn't allow someone to send countless post requests to server
def create_update():
    new_data = {
        'user': 1,
        'content': 'Another update' 
    }
    r = requests.post(BASE_URL+ENDPOINT, data=new_data)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

list_data = get_list()
# print(list_data)
spec_content = get_detail_by_content(content='Hello there!')
# print(spec_content)
create_update()