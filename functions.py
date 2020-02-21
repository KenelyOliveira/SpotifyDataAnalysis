import json
import requests
import base64

def format_query(query):
    return query.replace(" ", "%20")

def load_config():
    with open("config/appsettings.json", encoding = "utf8") as settings:
        return json.load(settings)

def get_paths(type):
    for data in load_config()["data"]:
        if data["type"] == type:
            return data["paths"]
    return ""

def load_data(type):
    #TODO: fix this logic
    if (type == "streaming_history"):
        data = []
        for path in get_paths(type):
            with open(path, encoding = "utf8") as settings:
                data += json.load(settings)
        return data

    with open(get_paths(type)[0], encoding = "utf8") as settings:
         return json.load(settings)

def print_json(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))    

def get_node(data, value):
    for d in data:
        if d["name"] == value:
            return d
    return {}

def get_artistByGenre(name):
    return lastfm_get({
        'method': 'artist.getinfo',
        'artist': format_query(name)
    })

def lastfm_get(payload):
    config = load_config()
    lastfm_gateway = config["gateways"][0]
    
    headers = { 'user-agent': config["application"]["user_agent"] }
    
    payload['api_key'] = lastfm_gateway["api_key"]
    payload['format'] = 'json'

    response = requests.get(lastfm_gateway["url"], headers = headers, params = payload)
    return response

def get_authorization(client_id, client_secret):
    return   (base64.encodebytes(('%s:%s' % (client_id,client_secret)).encode('utf-8')).decode().strip()).replace('\n', '')