import json
import requests

ENDPOINT = "http://127.0.0.1:8000/api/status/endpoint/"

def do(method='get', data={}, id=1, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT + "?id=" + str(id), data=data)
    print(r.text)
    return r

do(data={'id': 9}, id=9)
do(method='delete' data={'id': 9})
do(method='put', data={'id': 9, 'content': 'updated content', 'user':1})
do(method='post', data={'content': 'updated content', 'user':1})