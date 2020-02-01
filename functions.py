import json

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
        data = ""
        for path in get_paths(type):
            with open(path, encoding = "utf8") as settings:
                data += str(json.load(settings)).strip('[').strip(']')
        return "[%s]" % data

    with open(get_paths(type)[0], encoding = "utf8") as settings:
         return json.load(settings)

def print_json(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))    


# def lastfm_get(payload):
#     # define headers and URL
#     headers = {'user-agent': USER_AGENT}
#     url = 'http://ws.audioscrobbler.com/2.0/'

#     # Add API key and format to the payload
#     payload['api_key'] = API_KEY
#     payload['format'] = 'json'

#     response = requests.get(url, headers=headers, params=payload)
#     return response    