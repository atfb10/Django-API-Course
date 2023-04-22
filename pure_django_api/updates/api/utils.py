'''
adam forestier
april 22, 2023
'''
import json

def is_json(data):
    try:
        is_valid = json.loads(data)
    except ValueError:
        is_valid = False
    return is_valid