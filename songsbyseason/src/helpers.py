import json
import requests
import base64

def format_query(query):
    return query.replace(' ', '%20')

def load_config():
    with open('./config/appsettings.json', encoding = 'utf8') as settings:
        return json.load(settings)

def get_paths(type):
    for data in load_config()['data']:
        if data['type'] == type:
            return data['paths']
    return ''

def load_data(type):
    data = []
    for path in get_paths(type):
        with open(path, encoding = 'utf8') as settings:
            data.append(json.load(settings))
    return data

def print_json(obj):
    print(json.dumps(obj, sort_keys = True, indent = 4))    

def get_node(data, key, value):
    for d in data:
        if d[key] == value:
            return d
    return None

def get_payload(name):
    return {'method':'artist.getinfo','artist':format_query(name)}

def format_basicAuth(client_id, client_secret):
    return (base64.encodebytes(('%s:%s' % (client_id,client_secret)).encode('utf-8')).decode().strip()).replace('\n', '')
